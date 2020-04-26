<template>
    <div class="tac">
        <canvas ref="canvas">
            您的浏览器不支持canvas
        </canvas>
        <div id="controller">
            <div id="black_btn" class="color_btn color_btn_selected"></div>
            <div id="blue_btn" class="color_btn"></div>
            <div id="green_btn" class="color_btn"></div>
            <div id="red_btn" class="color_btn"></div>
            <div id="orange_btn" class="color_btn"></div>
            <div id="yellow_btn" class="color_btn"></div>

            <div id="clear_btn" class="op_btn" @click="clear">清 除</div>
            <div class="clearfix"></div>
        </div>
    </div>
</template>

<script>
export default{
    data(){
        return {
            canvas: null,
            context: null,
            canvasWidth: null,
            canvasHeight: null,
            maxLineWidth: 30,
            minLineWidth: 1,
            maxStrokeV: 10,
            minStrokeV: 0.1,
            lastLoc: {},
            lastTimestamp: 0,
            lastLineWidth: -1,
        }
    },

    computed: {
        
    },

    methods: {
        calcLineWidth(t, s) {
            let v = s / t;
            let resultLineWidth;
            if (v <= this.minStrokeV) {
                resultLineWidth = this.maxLineWidth;
            } else if (v >= this.maxStrokeV) {
                resultLineWidth = this.minLineWidth;
            } else {
                resultLineWidth = this.maxLineWidth - (v - this.minStrokeV) / (this.maxStrokeV - this.minStrokeV) * (this.maxLineWidth - this.minLineWidth)
            }

            if (this.lastLineWidth == -1) {
                return resultLineWidth;
            }
            return resultLineWidth * 1 / 3 + this.lastLineWidth * 2 / 3;
        },

        calcDistance(loc1, loc2) { // 计算两点间距离
            return Math.sqrt((loc1.x - loc2.x) * (loc1.x - loc2.x) + (loc1.y - loc2.y) * (loc1.y - loc2.y));
        },

        windowToCanvas(x, y) { // 坐标系转换
            let bbox = this.canvas.getBoundingClientRect();
            return {
                x: Math.round(x - bbox.left),
                y: Math.round(y - bbox.top)
            }
        },

        beginStroke(point) {
            this.isMouseDown = true;
            this.lastLoc = this.windowToCanvas(point.x, point.y)
            this.lastTimestamp = new Date().getTime();
        },

        endStroke() {
            this.isMouseDown = false;
        },

        moveStroke(point) {
            let curLoc = this.windowToCanvas(point.x, point.y);
            let curTimestamp = new Date().getTime();
            let s = this.calcDistance(curLoc, this.lastLoc);
            let t = curTimestamp - this.lastTimestamp;
            let lineWidth = this.calcLineWidth(t, s);

            this.context.beginPath();
            this.context.moveTo(this.lastLoc.x, this.lastLoc.y);
            this.context.lineTo(curLoc.x, curLoc.y);

            this.context.strokeStyle = this.strokeColor;
            this.context.lineWidth = lineWidth;
            this.context.lineCap = 'round';
            this.context.lineJoin = 'round';
            this.context.stroke();

            this.lastLoc = curLoc;
            this.lastTimestamp = curTimestamp;
            this.lastLineWidth = lineWidth;
        },

        drawGrid() {
            this.context.save();
            this.context.strokeStyle = 'rgb(230,11,9)';
            this.context.beginPath();
            this.context.moveTo(3, 3);
            this.context.lineTo(this.canvasWidth - 3, 3);
            this.context.lineTo(this.canvasWidth - 3, this.canvasHeight - 3);
            this.context.lineTo(3, this.canvasHeight - 3);
            this.context.closePath();
            this.context.lineWidth = 6;
            this.context.stroke();
            this.context.beginPath();
            this.context.moveTo(0, 0);
            this.context.lineTo(this.canvasWidth, this.canvasHeight);
            this.context.moveTo(this.canvasWidth, 0);
            this.context.lineTo(0, this.canvasHeight);
            this.context.moveTo(this.canvasWidth / 2, 0);
            this.context.lineTo(this.canvasWidth / 2, this.canvasHeight);
            this.context.moveTo(0, this.canvasHeight / 2);
            this.context.lineTo(this.canvasWidth, this.canvasHeight / 2);
            this.context.lineWidth = 1;
            this.context.stroke();
            this.context.closePath();
            this.context.restore();
        },

        clear (){
            this.context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
            this.drawGrid();
        },

        init(){
            this.canvasWidth = Math.min(800, window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth - 20);
            this.canvasHeight = this.canvasWidth;

            this.strokeColor = 'black';
            this.isMouseDown = false;
            this.lastLoc = {
                x: 0,
                y: 0
            };
            

            this.canvas = this.$refs.canvas;
            this.context = this.canvas.getContext('2d');

            this.canvas.width = this.canvasWidth;
            this.canvas.height = this.canvasHeight;

            this.maxLineWidth = this.canvasWidth / 800 * 30;

            this.canvas.onmousedown = (e)=> {
                e.preventDefault();
                this.beginStroke({
                    x: e.clientX,
                    y: e.clientY
                })
            }

            this.canvas.onmouseup = (e)=> {
                e.preventDefault();
                this.endStroke()
            }

            this.canvas.onmouseout = (e)=> {
                e.preventDefault();
                this.endStroke()
            }

            this.canvas.onmousemove = (e)=> {
                e.preventDefault();
                if (this.isMouseDown) {
                    this.moveStroke({
                        x: e.clientX,
                        y: e.clientY
                    })
                }
            }

            this.canvas.addEventListener("touchstart", (e)=> {
                e.preventDefault();
                let touch = e.touches[0];
                this.beginStroke({
                    x: touch.pageX,
                    y: touch.pageY
                })
            });

            this.canvas.addEventListener("touchmove", (e)=> {
                e.preventDefault();
                if (this.isMouseDown) {
                    let touch = e.touches[0];
                    this.moveStroke({
                        x: touch.pageX,
                        y: touch.pageY
                    })
                }
            });

            this.canvas.addEventListener("touchend", (e)=> {
                e.preventDefault();
                this.endStroke();
            });

            this.drawGrid()

        }
    },

    mounted(){
        this.init()
    }
}
    
</script>

<style lang="less" scoped>
    #canvas {
        display: block;
        margin: 0 auto;
    }

    #controller {
        margin: 0 auto;
    }

    .op_btn {
        float: right;
        margin: 10px 0 0 10px;
        border: 2px solid #aaa;
        width: 80px;
        height: 40px;
        line-height: 40px;
        font-size: 20px;
        text-align: center;
        border-radius: 5px 5px;
        cursor: pointer;
        background-color: white;
        font-weight: bold;
        font-family: Microsoft Yahei, Arial;
    }

    .op_btn:hover {
        background-color: #def;
    }

    .clearfix {
        clear: both;
    }

    .color_btn {
        float: left;
        margin: 10px 10px 0 0;
        border: 5px solid white;
        width: 40px;
        height: 40px;
        border-radius: 5px 5px;
        cursor: pointer;
    }

    .color_btn:hover {
        border: 5px solid violet;
    }

    .color_btn_selected {
        border: 5px solid blueviolet;
    }

    #black_btn {
        background-color: black;
    }

    #blue_btn {
        background-color: blue;
    }

    #green_btn {
        background-color: green;
    }

    #red_btn {
        background-color: red;
    }

    #orange_btn {
        background-color: orange;
    }

    #yellow_btn {
        background-color: yellow;
    }
</style>
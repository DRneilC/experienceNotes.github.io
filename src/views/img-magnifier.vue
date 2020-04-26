<template>
    <div class="tac">
        <canvas ref="canvas" class="border mt-50"></canvas>
        <canvas ref="offCanvas" style="display: none"></canvas>
    </div>
</template>

<script>

import util from '../libs/util.js';

export default {
    data(){
        return {
            canvas: null,
            offCanvas: null,
            context: null,
            offContext: null,
            image: null,
            scale: null,
        }
    },

    methods: {
        init(){
            this.canvas = this.$refs.canvas;
            this.context = this.canvas.getContext('2d');

            this.offCanvas = this.$refs.offCanvas;
            this.offContext = this.offCanvas.getContext('2d');

            this.image = new Image();
            var point;
            var isMouseDown = false;

            this.canvas.width = 1152;
            this.canvas.height = 768;
            this.image.src = util.sourceUrl + '/imgs/img-lg.jpg';

            this.image.onload = ()=> {
                this.offCanvas.width = this.image.width;
                this.offCanvas.height = this.image.height;
                this.scale = this.offCanvas.width/this.canvas.width;

                this.context.drawImage(this.image, 0, 0, this.canvas.width, this.canvas.height);
                this.offContext.drawImage(this.image,0,0)
            }

            this.canvas.onmousedown = (e)=> {
                e.preventDefault()
                isMouseDown = true;
                point = this.windowToCanvas(e.clientX, e.clientY);
                this.drawCanvasWithMagnifier(true, point)
            }

            this.canvas.onmouseup = (e)=> {
                e.preventDefault()
                isMouseDown = false;
                this.drawCanvasWithMagnifier(false);
            }

            this.canvas.onmouseout = (e)=> {
                e.preventDefault()
                isMouseDown = false
                this.drawCanvasWithMagnifier( false )
            }

            this.canvas.onmousemove = (e)=> {
                e.preventDefault()
                if(isMouseDown){
                    point = this.windowToCanvas(e.clientX,e.clientY);
                    this.drawCanvasWithMagnifier(true,point);
                }

            }
        },

        windowToCanvas(x, y) {
            var bbox = this.canvas.getBoundingClientRect();
            return {
                x: x - bbox.left,
                y: y - bbox.top
            }
        },

        drawCanvasWithMagnifier(isShowMagnifier, point) {
            this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
            this.context.drawImage(this.image, 0, 0, this.canvas.width, this.canvas.height);

            if (isShowMagnifier) {
                this.drawMagnifier(point);
            }
        },

        drawMagnifier(point) {
            var mr = 200;
            //将缩小版图片上点击的位置映射到大图上
            var imageLG_cx = point.x * this.scale;
            var imageLG_cy = point.y * this.scale;

            //将大图上对应的点移动到圆心
            var sx = imageLG_cx - mr;
            var sy = imageLG_cy - mr;

            var dx = point.x - mr;
            var dy = point.y - mr;

            this.context.save();

            this.context.lineWidth = 10;
            this.context.strokeStyle = '#069';
            this.context.beginPath();
            this.context.arc(point.x, point.y, mr,0, 2*Math.PI, false);
            this.context.stroke();
            this.context.clip();
            this.context.drawImage(this.offCanvas, sx, sy, 2*mr, 2*mr,dx,dy,2*mr,2*mr);
            this.context.closePath();
            this.context.restore();
        }
    },

    mounted (){
        this.init()
    }
}
    
</script>
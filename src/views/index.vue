<template>
    <div>
        <canvas ref="canvas" id="canvas"></canvas>

        <div class="menu-tabs por tac height-100">
            <div class="menu-tab cup" v-for="(item, index) in tabs" :key="index" @click="routeTo(item.url)">{{item.name}}</div>
        </div>
    </div>
</template>
<script>    
    export default {
        data (){
            return {
                tabs: [
                    {
                        name: '手写',
                        url: 'handwriting',
                    },
                    {
                        name: '钟表',
                        url: 'clocks',
                    },
                    {
                        name: '图片查看器',
                        url: 'img-magnifier',
                    },
                    {
                        name: '图片缩放',
                        url: 'img-scale',
                    },
                    {
                        name: 'canvas颗粒',
                        url: 'line',
                    },
                ],

                canvas: null,
                context: null,
                screenW: null,
                screenH: null,
                stars: [],
                FPS: 50,
                numStars: 2000, // 还可以根据屏幕大小和星星数量的比例关系做一个取值

                intervalId: null,
            }
        },

        methods: {
            routeTo (url){
                this.$router.push(url)
            },

            init(){
                /** 
                * canvas 创建星空
                */

                //获取canvas
                this.canvas = this.$refs.canvas;
                // 设置画布大小
                this.render();
                //获取canvas执行上下文
                this.context = this.canvas.getContext('2d');
                // ===========组件应用层============
                //创建星星
                for (let i = 0; i < this.numStars; i++) {
                    let x = Math.round(Math.random() * this.screenW);
                    let y = Math.round(Math.random() * this.screenH);
                    let length = 1 + Math.random() * 2;
                    let opacity = Math.random();

                    // 创建星星实例
                    let star = {
                        x: x,
                        y: y,
                        length: length,
                        opacity: opacity,
                        factor: 1,
                        increment: Math.random() * 0.03,
                    }
                    this.stars.push(star);
                }

                // 星星闪动
                clearInterval(this.intervalId)
                this.intervalId = window.setInterval(this.animate, 1000 / this.FPS);
            },

            //对象原型方法
            /**
             * 画星星
             * 
             * @param context
             */
            draw (star, context) {
                this.context.rotate(Math.PI * 1 / 10);

                //save the context
                this.context.save();
                //move into the middle of the canvas,just make room
                this.context.translate(star.x, star.y);
                //change the opacity
                if (star.opacity > 1) {
                    star.factor = -1;
                } else if (star.opacity <= 0) {
                    star.factor = 1;

                    // 更新一次星星位置
                    star.x = Math.round(Math.random() * this.screenW);
                    star.y = Math.round(Math.random() * this.screenH);
                }

                // factor 控制方面，淡入淡出，每次重绘，星星的透明度都在变化
                star.opacity += star.increment * star.factor;

                this.context.beginPath();
                //画线
                for (var i = 5; i > 0; i--) {
                    this.context.lineTo(0, star.length);
                    this.context.translate(0, star.length);
                    this.context.rotate(Math.PI * 2 / 10);
                    this.context.lineTo(0, -star.length);
                    this.context.translate(0, -star.length);
                    this.context.rotate(-(Math.PI * 6 / 10));
                }

                this.context.lineTo(0, star.length);
                this.context.closePath();

                this.context.fillStyle = 'rgba(255,255,200, ' + star.opacity + ')';
                this.context.shadowBlur = 5;
                this.context.shadowColor = '#ffff33';
                this.context.fill();

                this.context.restore();
            },

            /**
             * 获取窗口大小信息
             */
            getScreenInfo() {
                let winWidth, winHeight;
                //获取窗口宽度
                if (window.innerWidth) {
                    winWidth = window.innerWidth;
                } else if ((document.body) && (document.body.clientWidth)) {
                    winWidth = document.body.clientWidth;
                }

                //获取窗口高度
                if (window.innerHeight) {
                    winHeight = window.innerHeight;
                } else if ((document.body) && (document.body.clientHeight)) {
                    winHeight = document.body.clientHeight;
                }

                //通过深入Document内部对body进行检测，获取窗口大小
                if (document.documentElement &&
                    document.documentElement.clientHeight &&
                    document.documentElement.clientWidth) {
                    winHeight = document.documentElement.clientHeight;
                    winWidth = document.documentElement.clientWidth;
                }

                // 将上述方法简化
                // screenW = window.innerWidth ||
                //     document.body.clientWidth ||
                //     document.documentElement.clientWidth;

                // screenH = window.innerHeight ||
                //     document.body.clientHeight ||
                //     document.documentElement.clientHeight;

                return {
                    'winWidth': winWidth,
                    'winHeight': winHeight
                }
            },

            /**
             * canvas设置，修复窗口变化，画布大小不变的问题
             */
            render() {
                //获取屏幕大小
                this.screenW = this.getScreenInfo().winWidth;
                this.screenH = this.getScreenInfo().winHeight;

                // 设置canvas
                // canvas.setAttribute('width', screenW);
                // canvas.setAttribute('height', screenH);

                this.canvas.width = this.screenW;
                this.canvas.height = this.screenH;

                window.addEventListener('resize', this.render);
            },

            /**
             * 星星闪动函数
             */
            animate() {
                this.context.clearRect(0, 0, this.screenW, this.screenH);
                for (let i = 0; i < this.stars.length; i++) {
                    let star = this.stars[i];

                    this.draw(star, this.context);
                }

                // window.requestAnimationFrame(animate);
            },

        },

        mounted (){
            this.init()
        },

        beforeDestroy (){
            console.log('beforeDestroy')
            clearInterval(this.intervalId)
        }
    };

</script>

<style lang="less" scoped>
    #canvas {
        position: absolute;
        left: 0;
        top: 0;
        background-color: #000;
    }

    .menu-tabs{
        font-size: 24px;
        color: white;
        padding-top: 100px;

        .menu-tab{
            border: 1px solid white;
            border-radius: 8px;
            padding: 8px 20px;
            margin: 15px auto;
            width: 200px;
        }
    }
</style>
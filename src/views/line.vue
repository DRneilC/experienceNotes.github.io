<template>
    <div>
        <canvas ref="theCanvas"></canvas>
    </div>
</template>

<script>
export default {
    data(){
        return {
            theCanvas: null,
            ctx: null,
            current_point: {},
            random_points: [],
            canvas_width: null,
            canvas_height: null,
            globalID: null,
        }
    },

    methods: {
        draw() {
            //清屏
            console.log('start')
            this.ctx.clearRect(0, 0, this.canvas_width, this.canvas_height);
            let i,pi,x_dist,y_dist,dist,w;

            //遍历点集合绘制线条，类似于握手问题，两个点只绘制一条线
            this.random_points.forEach((p, index) => {
                p.x += p.xa,        //按指定速度移动
                p.y += p.ya,
                //小球碰撞则速度取相反数
                p.xa *= p.x > this.canvas_width || p.x < 0 ? -1 : 1,
                p.ya *= p.y > this.canvas_height || p.y < 0 ? -1 : 1,
                this.ctx.fillRect(p.x - 0.5, p.y - 0.5, 1, 1);       //绘制点

                for(i = index + 1; i < this.all_points.length; i++ ) {
                    pi = this.all_points[i];
                    if(pi.x !== null && pi.y !== null) {
                        x_dist = p.x - pi.x;
                        y_dist = p.y - pi.y;
                        dist = x_dist * x_dist + y_dist * y_dist;
                        //当两点距离小于极限距离时会产生连线，当第二个点是鼠标所产生点时，第一个点在范围内会产生向鼠标点的速度，产生吸附效果
                        dist < pi.max && (pi === this.current_point && dist >= pi.max / 2 && (p.x -= 0.03 * x_dist, p.y -= 0.03 * y_dist));
                        //根据距离计算连线的透明度，使过度效果流畅
                        w = (pi.max - dist) / pi.max;
                        this.ctx.beginPath();
                        this.ctx.lineWidth = w / 2;
                        this.ctx.strokeStyle = `rgba(110,110,110,${w + 0.2})`;
                        this.ctx.moveTo(p.x, p.y);
                        this.ctx.lineTo(pi.x, pi.y);
                        this.ctx.stroke();
                    }
                }
            }), this.animate();
        },

        animate (){
            this.globalID = requestAnimationFrame(this.draw)
        },

        init(){
            this.theCanvas = this.$refs.theCanvas;
            this.ctx = this.theCanvas.getContext('2d');
            this.current_point = {
                x: null, //当前鼠标x
                y: null, //当前鼠标y
                max: 20000,
            };

            this.canvas_width = this.theCanvas.width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
            this.canvas_height = this.theCanvas.height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
            this.random_points = [];
            this.all_points = [];

            this.theCanvas.style = "position: fixed; top: 0px; left: 0px;";

            //绑定事件，判断是否添加鼠标这个点
            window.onmousemove = e => {
                e = e || window.event;
                this.current_point.x = e.clientX;
                this.current_point.y = e.clientY;
            };
            window.onmouseout = () => {
                this.current_point.x = null;
                this.current_point.y = null;
            };
            

            //随机生成100个点
            for(let i = 0; i < 100; i++ ) {

                let x = Math.random() * this.canvas_width,   //初始坐标
                    y = Math.random() * this.canvas_height,
                    xa = 2 * Math.random() - 1,         //x速度
                    ya = 2 * Math.random() - 1,         //y速度
                    max = 6000;                         //会产生连线的距离的平方

                this.random_points[i] = {x, y, xa, ya, max};
            }
            //将鼠标的点添加至点集合中
            this.all_points = [...this.random_points, this.current_point];

            //只是背景特效-所以延迟执行
            setTimeout(this.draw, 100);
        }
    },

    mounted(){
        this.init()
    },

    beforeDestroy (){
        console.log('beforeDestroy line')
        cancelAnimationFrame(this.globalID)
    }
}
 
</script>
<template>
    <div>
        <div class="tac mt-50">
            <canvas ref="clock" width="200" height="200"></canvas>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            canvas: null,
            context: null,
            width: null,
            height: null,
            r: null,
            rem: null,
        }
    },

    methods: {
        drawBackGround () {
            this.context.save();
            this.context.beginPath();
            this.context.translate(this.r, this.r);
            this.context.lineWidth = 10 * this.rem;
            this.context.arc(0, 0, this.r - this.context.lineWidth / 2, 0, Math.PI / 180 * 360, false);
            this.context.strokeStyle = '#000';
            this.context.stroke();
            this.context.closePath();

            //写数字
            this.context.beginPath();            
            const hourNumbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2];
            this.context.font = 18 * this.rem + 'px Arial';
            this.context.textAlign = 'center';
            this.context.textBaseline = 'middle';
            // this.context.fillStyle = "#00AAAA";
            hourNumbers.forEach((number, i) => {
                let rad = 2 * Math.PI / 12 * i;
                let x = Math.cos(rad) * (this.r - 30 * this.rem);
                let y = Math.sin(rad) * (this.r - 30 * this.rem);
                this.context.fillText(number, x, y);
            });
            this.context.closePath();

            //画刻度点
            for (let i = 0; i < 60; i++) {
                let rad = 2 * Math.PI / 60 * i;
                let x = Math.cos(rad) * (this.r - 18 * this.rem);
                let y = Math.sin(rad) * (this.r - 18 * this.rem);
                this.context.beginPath();
                if (i % 5 === 0) {
                    this.context.fillStyle = '#000';
                    this.context.arc(x, y, 2 * this.rem, 0, 2 * Math.PI, false);
                } else {
                    this.context.fillStyle = '#ccc';
                    this.context.arc(x, y, 2 * this.rem, 0, 2 * Math.PI, false);
                }
                this.context.fill();
            }
            this.context.closePath();
        },

        //画时针
        drawHour (hour, minute) {
            this.context.save();
            this.context.beginPath();

            let hrad = 2 * Math.PI / 12 * hour;
            let mrad = 2 * Math.PI / 12 / 60 * minute;

            this.context.rotate(hrad + mrad);
            this.context.lineWidth = 6 * this.rem;
            this.context.lineCap = 'round';
            this.context.strokeStyle = '#000';
            this.context.moveTo(0, 10 * this.rem);
            this.context.lineTo(0, -this.r / 2);
            this.context.stroke();
            this.context.closePath();
            this.context.restore();
        },

        //画分针
        drawMinute (minute) {
            this.context.save();
            this.context.beginPath();

            let mrad = 2 * Math.PI / 60 * minute;
            this.context.rotate(mrad);
            this.context.lineWidth = 3 * this.rem;
            this.context.lineCap = 'round';
            this.context.strokeStyle='#000';
            this.context.moveTo(0, 10 * this.rem);
            this.context.lineTo(0, -this.r + 30 * this.rem);
            this.context.stroke();
            this.context.closePath();
            this.context.restore();
        },

        //画秒针
        drawSecond (second) {
            this.context.save();
            this.context.beginPath();
            this.context.fillStyle = '#c14543';

            let srad = 2 * Math.PI / 60 * second;
            this.context.rotate(srad);
            this.context.moveTo(-2 * this.rem, 20 * this.rem);
            this.context.lineTo(2 * this.rem, 20 * this.rem);
            this.context.lineTo(1, -this.r + 18 * this.rem);
            this.context.lineTo(-1, -this.r + 18 * this.rem);
            this.context.fill();
            this.context.closePath();
            this.context.restore();
        },

        //画固定点（螺丝）
        drawDot () {
            this.context.beginPath();
            this.context.fillStyle = '#fff';
            this.context.arc(0, 0, 3 * this.rem, 0, Math.PI / 180 * 360, false);
            this.context.fill();
            this.context.closePath();
        },

        //时间走起来
        draw (){
            this.context.clearRect(0, 0, this.width, this.height);
            let now = new Date();
            let hour = now.getHours();
            let minute = now.getMinutes();
            let second = now.getSeconds();

            this.drawBackGround();
            this.drawHour(hour, minute);
            this.drawMinute(minute);
            this.drawSecond(second);
            this.drawDot();
            this.context.restore();
        },

        init (){
            this.canvas = this.$refs.clock;
            this.context = this.canvas.getContext('2d');
            //canvas.height也能获取到
            // canvas.height = 300;
            // canvas.width = 300;
            // console.log(canvas.width)

            this.width = this.context.canvas.width;
            this.height = this.context.canvas.height;
            this.r = this.width / 2;
            //设置时钟的缩放比例，原始大小200
            this.rem = this.width / 200;

            this.draw();
            setInterval(this.draw, 1000);

            // let getNow = ()=>{
            //     let now = new Date();
            //     let hour = now.getHours();
            //     let minute = now.getMinutes();
            //     let second = now.getSeconds();
            // }
        }
    },

    mounted(){
       this.init()
    }

}
   
</script>
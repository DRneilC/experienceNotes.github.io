<template>
    <div>
        <canvas ref="canvas" style="display:block;margin:0 auto;border:1px solid #aaa;">您的浏览器尚不支持canvas</canvas>
        <input type="range" ref="scaleRange" min="0.5" max="3.0" step="0.01" value="1.0" style="display:block;margin:20px auto;width:800px">
        <canvas ref="watermarkCanvas" style="display:none;margin:0 auto;border:1px solid #aaa;">
            您的浏览器尚不支持canvas
        </canvas>
    </div>
</template>

<script>
import util from '../libs/util.js';

export default {
    data (){
        return {
            canvas: null,
            context: null,
            slider: null,
            watermarkCanvas: null,
            watermarkContext: null,
        }
    },

    methods: {
        init () {
            this.canvas = this.$refs.canvas;
            this.context = this.canvas.getContext('2d');
            this.slider = this.$refs.scaleRange;

            this.watermarkCanvas = this.$refs.watermarkCanvas;
            this.watermarkContext = this.watermarkCanvas.getContext("2d");

            this.canvas.width = 1152;
            this.canvas.height = 768;

            let scale = 1.0;
            let image = new Image();
            image.src = util.sourceUrl + '/imgs/img-lg.jpg';

            image.onload = ()=> {
                this.drawImage(image, scale);
                this.slider.onmousemove = ()=> {
                    scale = this.slider.value;
                    this.drawImage(image, scale)
                }
            }

            //设置水印canvas
            this.watermarkCanvas.width = 600;
            this.watermarkCanvas.height = 100;

            this.watermarkContext.font = "bold 50px Arial";
            this.watermarkContext.lineWidth=1;
            this.watermarkContext.fillStyle='rgba( 255 , 255 , 255 , 0.5 )';
            this.watermarkContext.textBaseline='middle';
            this.watermarkContext.fillText('== 你喊呼儿嘿呦 ==', 20, 50);
        },

        drawImage(image, scale) {
            let imageWidth = 1152 * scale;
            let imageHeight = 768 * scale;

            let x = (this.canvas.width - imageWidth) / 2;
            let y = (this.canvas.height - imageHeight) / 2;

            this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
            this.context.drawImage(image, x, y, imageWidth, imageHeight);

            this.context.drawImage(this.watermarkCanvas, this.canvas.width-this.watermarkCanvas.width, this.canvas.height-this.watermarkCanvas.height);
        }
    },

    mounted (){
        this.init()
    }
}
   
</script>
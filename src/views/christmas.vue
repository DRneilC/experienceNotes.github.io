<template>
    <div>
        <div class="box" ref="box" :style="contentStyleObj">
            <div class="con">
                <div class="fz-base mb-80">亲爱的小姐姐，有一个小哥哥让我给我带句话，</div>
                <div class="tac mb-80">Honey！<br/>Merry Christmas</div>
                <div class="fz-base tar">希望我们两个新的一年，平平安安，顺顺利利！</div>
            </div>

            <audio ref="myNoticeVoice">
                <source src="http://images.drneilc.top/jingle_bell.mp3">
            </audio>
        </div>

        <div class="marsk" ref="marsk" v-if="showMarsk">
            <div class="toPlay" @click="palyByHand()">
                <div style="margin-left: 12px;">&#9658</div>
            </div>
        </div>
    </div>
</template>

<script>
import '../../static/js/snow.src.js';
import util from '../libs/util';

export default {
    data(){
        return {
            music: null,
            marsk: null,
            showMarsk: false,
            contentStyleObj: {},
        }
    },

    methods: {
        init (){
            this.music = this.$refs.myNoticeVoice

            var promise = this.music.play();

            if (promise !== undefined) {
                promise.then(() => {
                    console.log('auto play')
                    // Auto-play started
                    this.music.play()
                }).catch( error => {
                    console.log(error.name)
                    // Auto-play was prevented
                    // Show a UI element to let the user manually start playback
                    this.showMarsk = true
                })
            }
        },

        palyByHand() {
            this.music.play();
            this.showMarsk = false
        },

        getHeight (){
            this.contentStyleObj.height = util.getViewportSize().height + 'px';
        }
    },

    mounted (){
        this.init()
    },

    created(){
        window.addEventListener('resize', this.getHeight);
        this.getHeight()
    },

    destroyed(){
        window.removeEventListener('resize', this.getHeight)
    }
    
}
</script>

<style scoped>

.box{
    background: white url('https://pubresource.zaopiaowang.com/201812241057447536532_37.jpg') top center no-repeat; 
    /*background: rgba(255, 0, 0, 0);*/
    background-size:  cover;
    max-width: 1920px;
    margin: 0 auto;
    height: 100%;
    color: #FFFFFF;
    font: bold 100px/normal 'microsoft yahei';
    position: relative;
}
.box .con{
    width: 1200px;
    margin: 0 auto;
    padding: 9% 0 0;
    text-shadow: 6px 6px 6px rgba(255, 0, 0, .8);
}

.marsk {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    text-align: center;
    background: rgba(0, 0, 0, .3);
}

.marsk .toPlay{
    width: 100px;
    height: 100px;
    line-height: 100px;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-top: -50px;
    margin-left: -50px;
    border-radius: 50%;
    border: 4px solid white;
    font-size: 60px;
    cursor: pointer;
    color: rgba(255, 255, 255, .8);
}

.fz-base{
    font-size: 36px;
}

.mb-80{
    margin-bottom: 80px;
}

</style>
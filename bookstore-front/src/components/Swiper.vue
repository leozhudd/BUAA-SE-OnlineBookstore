<template>
    <div id="hy-swiper">
        <div class="swiper" @touchstart="touchStart" @touchmove="touchMove" @touchend="touchEnd">
            <slot></slot>
        </div>
        <slot name="indicator">
        </slot>
        <div class="indicator">
            <slot name="indicator" v-if="showIndicator && slideCount>1">
                <div v-for="(item, index) in slideCount" class="indi-item"
                :class="{active: index === currentIndex-1}" :key="index"></div>
            </slot>
        </div>
    </div>
</template>

<script>
  export default{
      name: "Swiper",
      props: {
          interval: {
              type: Number,
              default: 3000
          },
          animDuration: {
              type: Number,
              default: 300
          },
          moveRatio: {
              type: Number,
              default: 0.25
          },
          showIndicator: {
              type: Boolean,
              default: true
              //required: true
          }
      },
      data: function() {
          return {
              slideCount: 0, //元素个数
              totalWidth: 0, //swiper的宽度
              swiperStyle: {}, //swiper样式
              currentIndex: 1, //当前的index
              scrolling: false, //是否正在滚动
          }
      },
      mounted: function () {
          setTimeout(() => {
              //操作DOM，在前后添加Slide
              this.handleDom();
              //开启定时器
              this.startTimer();
          }, 100)
      },
      methods: {
          //定时器操作
          startTimer: function () {
              this.playTimer = window.setInterval(() => {
                this.currentIndex++;
                this.scrollContent(-this.currentIndex * this.totalWidth);
              }, this.interval)
          },
          stopTimer: function () {
              window.clearInterval(this.playTimer);
          },

          //滚动到正确的位置
          scrollContent: function (currentPosition) {
              //设置正在滚动
              this.scrolling = true;

              //开始滚动动画
              this.swiperStyle.transition = 'transform'+ this.animDuration + 'ms';
              this.setTransform(currentPosition);
              //判断滚动位置
              this.checkPosition();
              //滚动完成
              this.scrolling = false;
          },

          //校验正确的位置
          checkPosition: function() {
              window.setTimeout(() => {
                  //校验正确的位置
                  this.swiperStyle.transition = '0ms';
                  if (this.currentIndex >= this.slideCount + 1) {
                      this.currentIndex = 1;
                      this.setTransform(-this.currentIndex * this.totalWidth);
                  } else if (this.currentIndex <= 0) {
                      this.currentIndex = this.slideCount;
                      this.setTransform(-this.currentIndex * this.totalWidth);
                  }
                  //结束移动后的回调
                  this.$emit('transitionEnd', this.currentIndex-1);
              }, this.animDuration)
          },
          //
          setTransform: function (position) {
              
          }
      }
  }
</script>
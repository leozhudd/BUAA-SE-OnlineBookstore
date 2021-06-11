<template>
  <el-container>
    <el-aside width="200px">
      <span></span>
      <span>img</span>
    </el-aside>
    <el-container>
      <el-main>
        <span>{{name}}</span>
        <span>{{price | showPrice}}</span>
        <span>
          <button @click="increment">+</button>
          <!--<input class="quantity" v-model="counter" @blur="changeCount"> -->
          {{count}}
          <button @click="decrement">-</button>
        </span>

      </el-main>
      <el-footer style="height: 40px">
          <button @click="moveOut" id="move-out">移除</button>
      </el-footer>
    </el-container>
  </el-container>
</template>

<script>
export default {
    name: "shopitem",
    data : function() {
        return {
        }
    },
    props: {
        id: String,
        name: String,
        price: Number,
        count: Number,
        img: String,
    },
    filters: {
        showPrice(price) {
            return '￥' + price.toFixed(2)
        }
    },
    methods: {
      increment() {
        this.$emit('click-add');
      },
      decrement() {
        this.$emit('click-sub');
      },
      moveOut() {
        this.$emit('click-moveout');
      },
     /* changeCount() {
        this.$emit('count-blur', counter);
      }*/
    }
}
</script>

<style>
  .quantity {
      width: 10px;
  }
  #move-out {
    position: absolute;
    right: 30px;
    bottom: 8px;
  }
  .el-footer {
    background-color: #fabe64;
    color: #333;
    text-align: center;
    line-height: 40px;
    position: relative;
  }
  
  .el-aside {
    background-color: #d6873d;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  .el-main {
    background-color: #ffffff;
    color: #333;
    text-align: center;
    position: relative;
  }

  .el-main .span {
    position: absolute;
    width: 100px;
    margin: 10px;
  }

  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
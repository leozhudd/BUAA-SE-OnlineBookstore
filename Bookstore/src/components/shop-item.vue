<template>
  <el-container>
    <el-aside width="200px">img</el-aside>
    <el-container>
      <el-main>
        <span>{{name}}</span>
        <span>{{price | showPrice}}</span>
        <span>
          <button @click="countAdd">+</button>
          <input class="quantity" v-model="counter">
          <button @click="countSub">-</button>
        </span>

      </el-main>
      <el-footer style="height: 40px">
          delete
      </el-footer>
    </el-container>
  </el-container>
</template>

<script>
export default {
    name: "shopitem",
    data() {
        return {
            counter: 1,
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
    countAdd() {
        counter+=1;
    },
    countSub() {
        counter-=1;
    },
}
</script>

<style>
  .quantity {
      width: 10px;
  }

  .el-footer {
    background-color: #fabe64;
    color: #333;
    text-align: center;
    line-height: 40px;
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
    line-height: 120px;
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
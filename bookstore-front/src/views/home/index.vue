<template>
  <div id="home">
    <div style="margin-top: 15px;">
      <el-input placeholder="请输入关键字" v-model="keyword" size="small" class="input-with-select">
        <el-select v-model="select_key" slot="prepend" placeholder="请选择搜索类型">
         <el-option label="书名" value="book_name"></el-option>
         <el-option label="作者" value="book_author"></el-option>
        </el-select>
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
    </div>

    <div>
        
    </div>
  </div>
</template>

<script>
import {getHomeMultidata} from "@/network/home";

export default {
  data() {
    return {
      keyword: '',
      select_key: '',
      result: null
    }
  },
  created() {
    getHomeMultidata().then(res =>{
        console.log(res);
        this.result = res;
        //this.banners = res.data.banners;
    })
  },
  components: {

  }
}
</script>

<style>
  #home {
      width: 800px;
      margin: auto;
  }
  .el-select .el-input {
    width: 130px;
  }
  .input-with-select  .el-input-group__prepend{
    background-color: #fff;
  }
</style>
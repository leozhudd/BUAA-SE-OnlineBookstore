<template>
  <div id="home">
    <!-- <div style="margin-top: 15px;">
      <el-input placeholder="请输入关键字" v-model="keyword" size="small" class="input-with-select">
        <el-select v-model="select_key" slot="prepend" placeholder="请选择搜索类型">
         <el-option label="书名" value="book_name"></el-option>
         <el-option label="作者" value="book_author"></el-option>
        </el-select>
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
    </div> -->
    <div>
      <table>
        <tbody>
          <tr v-for="item in Allbooks" :key="item.pk">
            <td class="td-product">
              <img :src="item.fields.image" width="120" height="150" @click="toDetails(item)">
              <div class="product-info">
                <h6>{{item.fields.name}}</h6>
                <p>作者：{{item.fields.author}}</p>
                <p>出版社：{{item.fields.publisher}}</p>
                <p>单价：￥{{parseFloat(item.fields.price)}}</p>
                <p>分类：{{item.fields.category}}</p>
              </div>
              <div class="clearfix"></div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";

export default {
  data() {
    return {
      keyword: '',
      select_key: '',
      Allbooks: [
        {
          pk: '1',
          fields:{
            name: '魔理沙的魔法书',
            description: 'daze',
            price: 39.99,
            sold_count: 999,
            image: '',
            stock_count: 99,
            author: '雾雨魔理沙',
            publisher: '雾雨魔法店',
            category: '魔导书',
          }
        },
        {
          pk: '2',
          fields:{
            name: '魔理沙的魔法书',
            description: 'daze',
            price: 39.99,
            sold_count: 999,
            image: '',
            stock_count: 99,
            author: '雾雨魔理沙',
            publisher: '雾雨魔法店',
            category: '魔导书',
          }
        },
      ]
    }
  },
  created() {
    //this.getBooks();
  },
  methods: {
    getBooks() {
      request({
      method: 'get',
      url:'api/base/show_books/',
      }).then(res =>{
      console.log(res);
      if(!res.error_num) {
        this.Allbooks = res.data;
      } else {
        this.$message({
          type: 'error',
          message: '获取图书信息失败'+res.message
        })
      }
      }).catch(err => {
      this.$message({
        type: 'error',
        message: '获取图书信息失败'+res.message
      })
      })
    },
    toDetails(item) {
      //发送id，在详情页加载信息
      this.$router.push({path: '/details', query: {book_id: item.pk}});
    },
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
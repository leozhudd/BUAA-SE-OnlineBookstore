<template> 
  <div id="shoppingcart">
    <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选</el-checkbox>
      <div style="margin: 15px 0;"></div>
      <el-checkbox-group v-model="checkedBooks" @change="handleCheckedBooksChange">
        <el-checkbox v-for="book in books" :key="book.book_id">{{book.book_name}}</el-checkbox>
      </el-checkbox-group>
      <div v-for="item in books" :key="item.book_name">
        <shopitem :id="item.book_id"
                  :name="item.book_name" 
                  :price="item.book_price"
                  :count="item.book_count"
                  :img="item.book_img"
                  @click-add="countAdd(item)" @click-sub="countSub(item)" 
                  @click-moveout="moveBookOut(item.book_id)"></shopitem>
      </div>
  </div>
</template>


<script>
import shopitem from '@/components/shop-item';
import {request} from "@/network/request.js";

export default {
    name: "Shoppingcart",
    data() {
        return { 
            checkAll: false,
            checkedBooks: [],
            isIndeterminate: true,

            books: [{
                book_id: '',
                book_name: 'unix',
                book_price: 59.00,
                book_count: 1,
                book_img: ''
            },
            {
                book_name: 'csapp',
                book_price: 39.00,
                book_count: 1,
                book_img: ''
            }]
        }
    },
    
    methods:{
        created() {
            getBooks();
        },
        getBooks() {
            request({
              url: '/api/trade/show_shoppingcart/',
            }).then(res => {
              console.log(res);
              books = res.data; //试验中
            }).catch(err => {
              console.log(error);
            })
        },
        countAdd(item) {
            item.book_count++;
            let sendData = {
              book_id: item.book_id,
              book_count: item.book_count
            }
            request({
              url: '/api/trade/edit_shoppingcart/',
              data: sendData
            }).then(res => {
              console.log(res.message);
            }).catch(err => {
              console.log(error);

            })
        },
        countSub(item) {
            if (item.book_count>1){
                item.book_count--;
                let sendData = {
                book_id: item.book_id,
                book_count: item.book_count
                }
                request({
                  url: '/api/trade/edit_shoppingcart/',
                  data: sendData
                }).then(res => {
                  console.log(res.message);
                }).catch(err => {
                  console.log(error);
                })
            }
        },
        moveBookOut(bookid) {
            request({
              url: '/api/trade/del_from_shoppingcart/',
              data: {book_id: bookid}
            }).then(res => {
              console.log(res);
             //刷新
             
            }).catch(err => {
              console.log(error);
              //提示信息
            })
        },
       /* updateCount(item, counter) {
            console.log(item);
            item.book_count = counter;
            request({
              method: 'get',
              url: '/api/trade/edit_shoppingcart/',
              data: {'username':$store.state.onlineuser, 'book_id':item.book_id, 'book_count':item.book_count}
            }).then(res => {
              console.log(res);
             
            }).catch(err => {
              console.log(error);
            })
        }*/
        handleCheckAllChange(val) {
          this.checkedBooks = val ? books : [];
          this.isIndeterminate = false;
        },
        handleCheckedBooksChange(value) {
          let checkedCount = value.length;
          this.checkAll = checkedCount === this.books.length;
          this.isIndeterminate = checkedCount > 0 && checkedCount < this.books.length;
        }
    },
    components: {
        shopitem,
    }
}
</script>

<style>
  #shoppingcart {
      width: 800px;
      margin: auto;
  }

</style>
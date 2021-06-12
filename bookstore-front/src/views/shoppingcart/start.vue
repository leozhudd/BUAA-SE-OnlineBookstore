<template> 
  <div id="shoppingcart">
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
    
    created() {
      //if (store.state.isLogin) else{this.$router.push('/login')}
      this.getBooks();
    },
    methods:{
        getBooks() {
          let sendData = new FormData()
          console.log(sessionStorage.getItem("username"));
          sendData.append('username',sessionStorage.getItem("username"));
          request({
              method: 'get',
              url: '/api/trade/show_shoppingcart/',
              data: sendData
          }).then(res => {
              console.log(res);
              this.books = res.data;
          }).catch(err => {
              console.log(err);
          })
        },
        updateCount(item) {
          let sendData = new FormData()
          sendData.append('book_id', item.book_id)
          sendData.append('book_count', item.book_count)

          request({
            method: 'post',
            url: '/api/trade/edit_shoppingcart/',
            data: sendData
          }).then(res => {
            console.log(res.message);
          }).catch(err => {
            console.log(error);
          })
        },

        countAdd(item) {
            item.book_count++;
            updateCount(item);
        },
        countSub(item) {
            if (item.book_count>1){
                item.book_count--;
                updateCount(item);
            }
        },
        moveBookOut(bookid) {
            request({
              method: 'post',
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
    },
}
</script>

<style>
  #shoppingcart {
      width: 800px;
      margin: auto;
  }

</style>
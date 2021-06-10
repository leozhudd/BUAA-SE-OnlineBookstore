<template> 
  <div id="shoppingcart">

      <div v-for="item in books" :key="item.book_name">
        <shopitem :id="item.book_id"
                  :name="item.book_name" 
                  :price="item.book_price"
                  :count="item.book_count"
                  :img="item.book_img"></shopitem>
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

    getBooks() {
        request({
            method: 'get',
            url: '/api/trade/show_shoppingcart/',
            data: {'username':$store.state.onlineuser}
        }).then(res => {
            console.log(res);
            let books = JSON.parse(res); //试验中
        }).catch(err => {
            console.log(error);
        })
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
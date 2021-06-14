<template>
  <div id="order">
    <table>
      <tbody>
        <tr v-for="item in books" :key="item.book_id">
          <td class="td-product">
            <img :src="item.book_img" width="98" height="98">
            <div class="product-info">
              <h6>{{item.book_name}}</h6>
              <p>作者：{{item.book_author}}</p>
            </div>
            <div class="clearfix"></div>
          </td>
          <td class="td-num">
            单价：<div>{{parseFloat(item.book_price) | showPrice}}</div>
          </td>
          <td class="td-count">
            数量：<div>{{item.book_count}}</div>
          </td>
        </tr>
      </tbody>
    </table>
    <div>
      收件人姓名：<input v-model="contact_name">
      电话：<input v-model="contact_phone">
      收货地址：<input v-model="address">
      备注：<input v-model="memo">
    </div>
    <div>
      <button @click="cancelOrder">取消订单</button>
      <button @click="submitOrder">提交订单</button>
    </div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";

export default{
    name: 'Order',
    data() {
        return {
          books:[],
          memo: '',
          address: '',
          contact_name: '',
          contact_phone: '',
        }
    },
    created() {
      this.books=this.$route.params.orderlist;
    },
    filters: {
      showPrice(price) {
        if (!price) {
          return '';
        }
        return '￥' + price.toFixed(2);
      }
    },
    methods: {
      submitOrder() {
        let booklist = [];
        for (let i in this.books) {
            booklist.push(this.books[i].book_id);
        }
        console.log(booklist);
        let sendData = new FormData()
        sendData.append('book_list', booklist);
        sendData.append('memo', this.memo);
        sendData.append('address', this.address);
        sendData.append('contact_name', this.contact_name);
        sendData.append('contact_phone', this.contact_phone);

        request({
          method: 'post',
          url: '/api/trade/selected_books_preview/',
          data: sendData
        }).then(res => {
          console.log(res);
          if (!res.error_num) {
            this.$message({
              type: 'success',
              message: '订单提交成功'
            });
            //布局相同的确认收货页面，不可编辑
          } else {
            this.$message({
              type: 'error',
              message: '订单提交失败'+res.message
            });
          }
        }).catch(err => {
          console.log(err);
          this.$message({
            type: 'error',
            message: '订单提交失败'
          });
        })
      },
      cancelOrder() {
        //返回上一页
        this.$router.go(-1);
      },
    }

}
</script>

<style>
</style>
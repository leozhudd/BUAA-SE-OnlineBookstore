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
      <ul>
        <li>订单编号：{{order_sn}}</li>
        <li>收件人姓名：{{contact_name}}</li>
        <li>电话：{{contact_phone}}</li>
        <li>收货地址：{{address}}</li>
        <li>备注：{{memo}}</li>
        <li>总金额：{{totalPrice}}</li>
      </ul>
    </div>
    <div>
      <button v-if="!is_signed" @click="getReceived">确认收货</button>
      <button v-else>已完成</button>
      <button @click="goBack">返回</button>
    </div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";

export default{
    name: 'subOrder',
    data() {
        return {
          books:[],
          memo: '',
          address: '',
          contact_name: '',
          contact_phone: '',
          is_signed: false,
          order_id: '',
          totalPrice: 0.00
        }
    },
    props:{
      books: Array,
      memo: String,
      address: String,
      contact_name: String,
      contact_phone: String,
      is_signed: Boolean,
      order_id: Number,
      order_sn: String,
      totalPrice: Number,
      add_time: String,
      is_signed: Boolean,
      is_paid: Boolean,
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
      getReceived() {
        let sendData = new FormData()
        sendData.append('id', order_id);

        request({
          method: 'post',
          url: '/api/trade/set_order_received/',
          data: sendData
        }).then(res => {
          console.log(res);
          if (!res.error_num) {
            this.is_signed = true;
            this.$message({
              type: 'success',
              message: '确认收货成功'
            });
          } else {
            this.$message({
              type: 'error',
              message: '确认收货失败'+res.message
            });
          }
        }).catch(err => {
          console.log(err);
          this.$message({
            type: 'error',
            message: '确认收货失败'
          });
        })
      },
      goBack() {
        //返回
        this.$router.go(-2);
      },
    }

}
</script>

<style>
</style>
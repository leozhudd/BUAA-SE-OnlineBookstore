<template>
  <div id="myorders">
    <button @click="displayWaiting">待收货订单</button>
    <button @click="displayReceived">已完成订单</button>
    <div v-for="item in display" :key="item.id">
      <suborder 
      :books="item.book_list"
      :memo="item.memo"
      :address="item.address"
      :contact_name="item.contact_name"
      :contact_phone="item.contact_phone"
      :order_id="item.id"
      :order_sn="item.order_sn"
      :amount_price="item.amount_price"
      :add_time="item.add_time"
      :is_signed="item.is_signed"
      :is_paid="item.is_paid"></suborder>
    </div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";
import suborder from "../order/submitted.vue";

export default {
    name: 'Myorders',
    data() {
      return {
        display:[],
        waitings:[],
        receiveds:[],
        allorders: [
        {
          id: 21,
          order_sn: '151563133',
          address: '妖怪之山',
          contact_name: '射命丸文',
          contact_phone: '155515156',
          amount_price: '999.00',
          add_time: '2021-06-15',
          is_signed: false,
          is_paid: true,
          memo: '不要上山',
          book_list: [
            {
              book_name: '写真',
              book_price: '123',
              book_image: '',
              book_count: '2'
            },
            {
              book_name: '传播学',
              book_price: '123',
              book_image: '',
              book_count: '4'
            }
          ]
        },
        {
          id: 22,
          order_sn: '151563133',
          address: '妖怪之山',
          contact_name: '射命丸文',
          contact_phone: '155515156',
          amount_price: '999.00',
          add_time: '2021-06-15',
          is_signed: false,
          is_paid: true,
          memo: '不要上山',
          book_list: [
            {
              book_name: '写真',
              book_price: '123',
              book_image: '',
              book_count: '2'
            },
            {
              book_name: '传播学',
              book_price: '123',
              book_image: '',
              book_count: '4'
            }
          ]
        },
        ]
      }
    },
    created() {
      this.getOrders();
      this.display = this.allorders;
    },
    methods: {
        getOrders() {
          request({
            method: 'get',
            url: '/api/trade/all_orders_with_details/'
          }).then(res => {
            console.log(res);
            if (!res.error_num) {
              this.allorders = res.data;
              this.indexOfSigned();
              this.display = this.allorders;
            } else {
              this.$message({
                type: 'error',
                message: '获取订单信息失败'+res.message
              })
            }
          }).catch(err => {
            console.log(err);
            this.$message({
              type: 'error',
              message: '获取订单信息失败'
            })
          }) 
        },
        indexOfSigned() {
          let list = [];
          let list2 = [];
          for (let i in this.allorders) {
            if (this.allorders[i].is_signed) {
              list.push(this.allorders[i]);
            }else {
              list2.push(this.allorders[i]);
            }
          }
          this.waitings = list2;
          this.receiveds = list1;
        },
        displayReceived() {
          this.display = this.receiveds;
        },
        displayWaiting() {
          this.display = this.waitings;
        }
    },
    components: {
        suborder,
    }
}
</script>

<style>
</style>
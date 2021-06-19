<template>
<div id="myorders">
  <div class="container clearfix">
	  <div class="help-l fl">
		  <div class="help-item">
			  <div class="help-item-title">个人中心</div>
			  <div class="help-item-list">
				<ul>
				  <li><router-link to="/chgps">修改密码</router-link></li>
				</ul>
				<ul>
				  <li><router-link to="/myorders">订单管理</router-link></li>
				</ul>
			  </div>
		  </div>
	  </div>
  <div class="help-r fr">
    <div class="help-item-title">订单管理</div>
		<div class="help-item-list">
		  <span><a @click="displayAll">全部订单</a>|</span>
		  <span><a @click="displayWaiting">待收货订单</a>|</span>
  		<span><a @click="displayReceived">已完成订单</a>|</span>
		</div>
		<div v-for="item in display" :key="item.id">
		  <suborder 
      	:book_list="item.book_list"
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
        // {
        //   id: 21,
        //   order_sn: '151563133',
        //   address: '妖怪之山',
        //   contact_name: '射命丸文',
        //   contact_phone: '155515156',
        //   amount_price: '999.00',
        //   add_time: '2021-06-15',
        //   is_signed: false,
        //   is_paid: true,
        //   memo: '不要上山',
        //   book_list: [
        //     {
        //       book_name: '写真',
        //       book_price: '123',
        //       book_image: '',
        //       book_count: '2'
        //     },
        //     {
        //       book_name: '传播学',
        //       book_price: '123',
        //       book_image: '',
        //       book_count: '4'
        //     }
        //   ]
        // },
        // {
        //   id: 22,
        //   order_sn: '151563133',
        //   address: '妖怪之山',
        //   contact_name: '射命丸文',
        //   contact_phone: '155515156',
        //   amount_price: '999.00',
        //   add_time: '2021-06-15',
        //   is_signed: true,
        //   is_paid: true,
        //   memo: '不要上山',
        //   book_list: [
        //     {
        //       book_name: '写真',
        //       book_price: '123',
        //       book_image: '',
        //       book_count: '2'
        //     },
        //     {
        //       book_name: '传播学',
        //       book_price: '123',
        //       book_image: '',
        //       book_count: '4'
        //     }
        //   ]
        // },
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
          let list1 = [];
          let list2 = [];
          for (let i in this.allorders) {
            if (this.allorders[i].is_signed) {
              list1.push(this.allorders[i]);
            }else {
              list2.push(this.allorders[i]);
            }
          }
          this.waitings = list2;
          this.receiveds = list1;
        },
        displayAll() {
          this.display = this.allorders;
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
.help-item-title{
	font-size: 16px;
	font-weight: bold;
	border-bottom: 1px solid #ddd;
	height: 35px;
	line-height: 35px;
	background-color: #f7f7f7;
	position: relative;
}
.help-item-list{
	color: #666;
	padding: 5px 0 5px 40px;
	line-height: 30px;
	font-size: 14px;
	display: block;
	height: 100%;
}
.help-item-list .router-link-exact-active{
	color: #42b983;
}
blockquote, body, dd, div, dl, dt, fieldset, form, h1, h2, h3, h4, h5, h6, img, input, li, ol, p, table, td, textarea, th, ul {
  margin: 0;
  padding: 0;
}
a{ text-decoration:none;  color: #666;}
a:hover{ text-decoration:none; color:#46b448;} 
li{ list-style:none;}
i, em {
	font-style: normal;
}
.fl{ float:left;}
.fr{ float:right;}

.abs{
	position: absolute;
}
.clearfix:after{ content:""; clear:both; display:block;}
.clearfix{ *zoom:1;}
input{ outline:none; border:none;}
.container{
	width: 1200px;
	margin: 0 auto;
}
.help-l{
	width: 180px;
	border-top: 4px solid #999;
  margin-top: 40px;
}
.help-item{
	border: 1px solid #ddd;
	border-top: 0;
}
.help-r{
	border: 1px solid #ddd;
	width: 980px;
  margin-top: 40px;
}
</style>
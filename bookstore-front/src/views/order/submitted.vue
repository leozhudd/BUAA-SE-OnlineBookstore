<template>
  <div id="submitted">
    <div class="help-main">
			<div class="product-item clearfix">
				<div class="name fl">
					<span style="margin-left: 150px">商品</span>
				</div>
				<div class="attr fr">
					<ul class="clearfix">
						<li>价格</li>
						<li>数量</li>
						<!-- <li style="width: 110px">状态</li> -->
					</ul>
				</div>
			</div>
			<div class="pro" v-for="item in books" :key="item.book_name">
				<div class="product-attr">
					<div class="product-name fl">
						<div class="pic-thumb fl"><img class="middle" :src="item.book_image" @click="toDetails(item)"></div>
						<div class="product-title fl">
							<a class="ellipsis" @click="toDetails(item)">{{item.book_name}}</a><br>
							<!-- <span>传播学院</span> -->
						</div>
					</div>
					<div class="product-price fr">
						<ul class="clearfix">
							<li>{{parseFloat(item.book_price) | showPrice}}</li>
							<li>{{item.book_count}}</li>
						</ul>
					</div>
				</div>
			</div>
      <div class="order-info">
        <ul class="fl">
          <li>订单编号：{{order_sn}}</li>
          <li>收件人姓名：{{contact_name}}</li>
          <li>电话：{{contact_phone}}</li>
          <li>收货地址：{{address}}</li>
        </ul>
        <ul class="ct-info"> 
          <li>备注：{{memo}}</li>
          <li>总金额：{{amount_price}}</li>
        </ul>
        <ul class="fr">
          <li class="edit" style="width: 110px">
						<span v-if="!is_signed" @click="getReceived" class="confirm"><a href="#">确认收货</a></span>
            <span v-else class="complete">已完成</span>
					</li>
        </ul>
      </div>
	</div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";

export default{
    name: 'suborder',
    data() {
        return {
          books: this.book_list,
        }
    },
    props:{
      book_list: Array,
      memo: String,
      address: String,
      contact_name: String,
      contact_phone: String,
      order_id: Number,
      order_sn: String,
      amount_price: String,
      add_time: String,
      is_signed: Boolean,
      is_paid: Boolean,
    },
    created() {
      
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
        sendData.append('id', this.order_id);

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
			//刷新？
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
      toDetails(item) {
        //发送id，在详情页加载信息
        this.$router.push({path: '/details', query: {book_id: item.book_id}});
      },
    }

}
</script>

<style>
blockquote, body, dd, div, dl, dt, fieldset, form, h1, h2, h3, h4, h5, h6, img, input, li, ol, p, table, td, textarea, th, ul {
  margin: 0;
  padding: 0;
}
a{ text-decoration:none;  color: #666;}
a:hover{ text-decoration:none; color:#46b448;} 
li{ list-style:none;}
img{ border:none;}
i, em {
	font-style: normal;
}
.fl{ float:left;}
.fr{ float:right;}
.abs{
	position: absolute;
}
.ellipsis {
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}
.ct-info{
  width:200px;
  margin-left: 400px;
}
.middle{
	position: relative;
	top: 50%;
	transform: translateY(-50%);
	-webkit-transform: translateY(-50%);
	-moz-transform: translateY(-50%);
	-o-transform: translateY(-50%);
}
.hide{
	display: none;
}

h1,h2,h3,h4{ font-weight:normal;}
.clearfix:after{ content:""; clear:both; display:block;}
.clearfix{ *zoom:1;}
input{ outline:none; border:none;}
.container{
	width: 1200px;
	margin: 40px auto;
}
.order-info{
  color:#666;
  text-align: left;
  font-size: 14px;
  height:120px;
  line-height: 25px;
  padding-left: 90px;
}
.help-main{
	margin: 0 20px 30px;
  border-bottom: solid 1px #353333;
  border-top: solid 1px #353333;
}
.help-main h2{
	color: #00b050;
	font-size: 16px;
	height: 50px;
	line-height: 50px;
}
.help-main p{
	font-size: 14px;
	line-height: 50px;
}
.help-main img{
	width: 100%;
	max-width: 100%;
	height: auto;
}
/*商品栏目*/
.product-item{
	height: 30px;
	width: 100%;
	line-height: 30px;
	background-color: #FAFAFA;
	border-bottom: solid 1px #E6E6E6;
}
.product-item .name{
	padding-left: 10px;
}
.product-item span{
	color: #999;
}
.product-item li,.product-price ul li{
	float: left;
	text-align: center;
	width: 90px;
	color: #999;
	font-size: 14px;
}
/*商品详情*/
.product-attr{
	height: 125px;
	width: 100%;
	line-height: 100px;
	border-bottom: solid 1px #E6E6E6;
}
.product-name{
	width: 400px;
	height: 100px;
	padding-left: 95px;
}
.product-name .pic-thumb{
	width: 90px;
	height: 120px;
	margin-right: 20px;
}
.product-name .pic-thumb a{
	display: inline-block;
	width: 60px;
	height: 100px;
}
.product-name .product-title{
	padding-top: 15px;
	line-height: 20px;
	/* width: 300px; */

}
.product-name .product-title a{
	color: #666;
	font-size: 14px;
	display: block;
}
.product-name .product-title a:hover{
	color: #46b448;
	text-decoration: underline;
}
.product-title span{
	font-size: 14px;
	color: #999;
	margin-right: 10px;
}
.product-title span i{
	font-size: 18px;
	height: 30px;
	line-height: 30px;
	cursor: default;
}
.product-title span i.commend{
	background-color: #E84C3D;
	color: #FFF;
	font-size: 14px;
	padding: 0 2px;
}
li.edit{
	line-height: normal;
	padding-top: 6px;
}

li.edit span.line{
	height: 40px;
	width: 0;
	border-left: 1px solid #E6E6E6;
	padding: 0;
}
li.edit span a{
	color: white;
}
li.edit span{
	width: 80px;
	height: 30px;
	line-height: 30px;
	color: white;
  display: inline-block;
	padding: 4px 10px;
  text-align: center;
}
li.edit span.confirm{
	background-color: #DA4F49;
}
li.edit span.complete{
	background-color: #8f8e8e;
}
li.edit span i{
	font-size: 20px;
	color: #777;
}
li.edit span p{
	color: #777;
	line-height: 20px;
}
li.edit span:hover i,li.edit span:hover p{
	color: white;
}
/* li.edit span:last-child:hover{
	background-color: #DA4F49;
} */
</style>
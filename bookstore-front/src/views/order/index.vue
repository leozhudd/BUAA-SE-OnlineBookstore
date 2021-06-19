<template>
  <div id="order">
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
			<div class="pro" v-for="item in books" :key="item.book_id">
				<div class="product-attr">
					<div class="product-name fl">
						<div class="pic-thumb fl"><img class="middle" :src="item.book_img" @click="toDetails(item)"></div>
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
      <div class="order-form">
        <el-form :inline="true" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-form-inline">
          <el-form-item label="收件人" prop="contact_name" size="small">
            <el-input v-model="ruleForm.contact_name"></el-input>
          </el-form-item>
          <el-form-item label="电话" prop="contact_phone" size="small">
            <el-input v-model="ruleForm.contact_phone"></el-input>
          </el-form-item>
        </el-form>

        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="收货地址" prop="address" style="width: 80%; margin:10px auto;">
            <el-input type="textarea" v-model="ruleForm.address"></el-input>
          </el-form-item>
          <el-form-item label="备注" prop="memo" style="width: 80%; margin:25px auto;">
            <el-input type="textarea" v-model="ruleForm.memo"></el-input>
          </el-form-item>
          <span class="order-info">总计：{{totalPrice}}</span>
          <el-form-item>
            <el-button type="info" @click="cancelOrder" plain>取消订单</el-button>
            <el-button type="danger" @click="submitForm('ruleForm')">提交订单</el-button>
          </el-form-item>
        </el-form>
      </div>
		</div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";

export default{
    name: 'Order',
    data() {
        return {
          books:[
            // {
            //   book_id:'1',
            //   book_name:'csapp',
            //   book_author:'Author',
            //   book_price:39.00,
            //   book_count:2,
            //   book_img:'',
            // },
            // {
            //   book_id:'2',
            //   book_name:'csapp',
            //   book_author:'Author',
            //   book_price:39.00,
            //   book_count:2,
            //   book_img:'',
            // },
          ],
          totalPrice: this.getTotal(),
          comefrom:'',

        ruleForm: {
          memo: '',
          address: '',
          contact_name: '',
          contact_phone: '',
        },
        rules: {
          contact_name: [
            { required: true, message: '请输入收件人姓名', trigger: 'blur' },
          ],
          contact_phone: [
            { required: true, message: '请输入联系电话', trigger: 'blur' }
          ],
          address: [
            { required: true, message: '请输入收货地址', trigger: 'blur' }
          ],
        }
        }
    },
    created() {
      console.log(JSON.parse(this.$route.query.orderlist));
      this.books=JSON.parse(this.$route.query.orderlist);
      this.comefrom=this.$route.query.comefrom;
      this.totalPrice=this.getTotal();
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
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.submitOrder();
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      submitOrder() {
        let sendData = new FormData();
        let sendURL = '';

        if (this.comefrom === 'cart'){
          let booklist = [];
          for (let i in this.books) {
            booklist.push(this.books[i].book_id);
          }
          console.log(booklist);
          sendData.append('book_list', JSON.stringify(booklist));
          sendURL = '/api/trade/creat_new_order/';
        } else if (this.comefrom === 'details'){
          sendData.append('book_id', this.books[0].book_id);
          sendData.append('book_count', this.books[0].book_count);
          sendURL = '/api/trade/new_order_single_book/';
        }
        sendData.append('memo', this.ruleForm.memo);
        sendData.append('address', this.ruleForm.address);
        sendData.append('contact_name', this.ruleForm.contact_name);
        sendData.append('contact_phone', this.ruleForm.contact_phone);

        request({
          method: 'post',
          url: sendURL,
          data: sendData
        }).then(res => {
          console.log(res);
          if (!res.error_num) {
            this.$message({
              type: 'success',
              message: '订单提交成功'
            });
            this.$router.push('/');
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
      getTotal() {
        let totalprice = 0;
        for (let i in this.books) {
              // 总价累加
          totalprice += this.books[i].book_count * this.books[i].book_price;
        }
        return totalprice;
      }
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
input{ outline:none;}
.container{
	width: 1200px;
	margin: 40px auto;
}
.order-input{
  border: 1px solid #666;
}
.order-info{
  color:#666;
  text-align: left;
  font-size: 14px;
  height:150px;
  line-height: 25px;
  margin-bottom: 5px;
  padding-left: 90px;
}
.order-form {
  margin: 10px auto;
  width: 800px;
}
.help-main{
	margin: 10px auto;
  margin-bottom: 10px;
  border-bottom: solid 1px #353333;
  border-top: solid 1px #353333;
  width:1000px;
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
</style>
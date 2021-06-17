<template>
  <div id="details">
	<div class="submena clearfix">
		<router-link to="/">首页</router-link>
		<span>></span>
		<router-link to="/">{{book.category}}</router-link>
		<span>></span>
		<span>商品详情</span>
	</div>
	<div class="showall">
	  <!--img -->
	  <div class="showbot">
		  <img :src="book.image" width="300" height="400" />
    </div>
    <div class="tb-property">
      <div class="tr-nobdr">
        <h3>{{book.name}}</h3>
      </div>
		  <div class="txt-h">
        <span class="tex-o">作者&nbsp;&nbsp;&nbsp;{{book.author}}</span>
			  <span class="tex-o">出版社&nbsp;&nbsp;&nbsp;{{book.publisher}}</span>
      </div>
      <div class="glist" id="glist" data-monitor="goodsdetails_fenlei_click">
        <span>分类</span><a href="">{{book.category}}</a>
      </div>
      <div class="txt">
        <span class="nowprice">￥<a>{{book.price}}</a></span>
          <div class="cumulative">
            <span class="number ty1">累计销量<br /><em id="add_sell_num_363">{{book.sold_count}}</em></span>
          </div>
      </div>
      <div class="gcIpt">
        <span class="guT">数量</span>
        <input id="min" type="button" value="-" @click="countSub" />  
        <input id="text_box" type="text" value="1" v-model="book.count" style="width:30px; text-align: center; color: #0F0F0F;"/>  
        <input id="add"  type="button" value="+" @click="countAdd" />
        <span class="Hgt">库存（{{book.stock_count}}）</span>
      </div>
      <div class="nobdr-btns">
        <button class="addcart hu" @click="addtoCart"><img src="../../assets/images/shop.png" width="25" height="25"/>加入购物车</button>
        <button class="addcart yh" @click="orderIt"><img src="../../assets/images/ht.png" width="25" height="25"/>立即购买</button>
      </div>
      <div class="guarantee">
        <span>邮费：包邮&nbsp;&nbsp;支持货到付款</span>
      </div>
  	</div>       
    <!-- 商品介紹 -->                
      <div class="detail">
        <div class="active_tab" id="outer">
  			  <ul class="act_title_left act_active" id="tab">
						  <a href="#">图书介绍</a>
				  </ul>
			  	<div class="clear"></div>
			  </div>
			  <div id="content" class="active_list"> 
				  <div id="ui-a" class="ui-a">
					  {{book.description}}
				  </div>								  
        </div>
      </div>
  </div>
</div>
</template>

<script>
import {request} from "@/network/request.js";
export default{
    name: "",
    data() {
        return {
            book: {
                id: '1',
                name: '魔理沙的魔法书',
                description: 'daze',
                price: 39.99,
                sold_count: 999,
                image: '',
                stock_count: 99,
                author: '雾雨魔理沙',
                publisher: '雾雨魔法店',
                category: '魔导书',
                count: 1,
            }
        }
    },
    created() {
        //获取传入的参数
        let _this = this;
        this.book.id = this.$route.query.book_id;
         console.log(this.book.id);
        this.getTheBook();
    },
    methods:{
        getTheBook() {
          let sendData = new FormData()
          sendData.append('book_id',this.book.id);
          request({
            method: 'post',
            url: '/api/base/book_info/',
            data: sendData
          }).then(res => {
            if (!res.error_num) {
              let thebook = res.data[0].fields;
              this.book.name = thebook.name;
              this.book.description = thebook.description;
              this.book.price = thebook.price;
              this.book.sold_count = thebook.sold_count;
              this.book.image = thebook.image;
              this.book.stock_count = thebook.stock_count;
              this.book.author = thebook.author;
              this.book.publisher = thebook.publisher;
              this.book.category = thebook.category;
              //给book添加count属性
              this.$set(this.book,'count', 1);
            } else {
              this.$message({
                type: 'error',
                message: '获取图书信息失败'
              })
            }
          }).catch(err => {
            console.log(err);
            this.$message({
                type: 'error',
                message: '获取图书信息失败'
            })
          })
        },
        //立即下单
        orderIt() {
          if (this.$store.state.isLogin){
            let orderlist = [];
            let thisbook = {
              book_id: this.book.id,
              book_name: this.book.name,
              book_price: this.book.price,
              book_img: this.book.image,
              book_author: this.book.author,
              book_count: this.book.count,
            }
            orderlist.push(thisbook);
            this.$router.push({path:'/order', query:{orderlist: JSON.stringify(orderlist)}});
          } else {
            this.$message({
              type: 'info',
              message: '请先登录'
            })
            this.$router.push({path:'/login', query:{route_bkid: this.book.id}});
          }
        },
        //加购
        addtoCart() {
          let sendData = new FormData()
          sendData.append('book_id',this.book.id)
          sendData.append('book_count',this.book.count)
          console.log(sendData);

          request({
            method: 'post',
            url: '/api/trade/add_to_shoppingcart/',
            data: sendData
          })
          .then(res=>{
            console.log(res);
            if(!res.error_num)
            {
              this.$message({
                type: 'success',
                message: '加购成功'
              });
            }
            else
            {
              this.$message({
                type: 'error',
                message: '加购失败',
              });
            }
          }).catch(error=>{
            console.log(error);
            this.$message({
              type: 'error',
              message: error.message
            });
          });
        },
        countAdd() {
          this.book.count++;
        },
        countSub() {
          if (this.book.count>1)
            this.book.count--;
        },
        searchAuthor() {
            this.$router.push({name: 'Search', query:{book_author: this.book.author} })
        }
    }
}
</script>

<style>
#details{
    font-family: 'Microsoft YaHei';
    color:#666;
    font-size:12px;
}

.submena{
    width: 1200px;
    height: 30px;
    margin: 0 auto;
    text-align: left;
}
.submena a{
    color:#37ab40;
    line-height: 30px;
}

.showall{
	width: 1240px;
	margin: 0 auto;
	margin-top: 15px;
}
.tb-property{
	width:530px;
	height: 520px;
	margin-left: 50px;
	float: left;
}

.showbot{float: left;}

/* .tr-nobdr{
	margin-top: 20px;
	padding-bottom: 10px;
} */
.tr-nobdr h3{
	color: #171717;
	font-size: 28px;
	font-weight:400;
  text-align: left;
}
.txt{
	width: 520px;
	margin-top: 15px;
	overflow: hidden;
	background: #f8f8f8;
}
.nowprice{
	display: block;
	line-height: 100px;
	color: #f73a3a;
	font-size: 24px;
	float: left;
}
.nowprice a{
	font-size: 36px;
	color: #f73a3a;
}
.nowprice a:hover{text-decoration: none;}
.cumulative{
	float: right;
	
}
.number{
	float: left;
	margin-top: 30px;
	padding: 0px 10px;
	border-right: #e7e7e7 solid 1px;
	font-size: 14px;
	text-align: center;
	color: #bfbfbf;
}
.number em{
	color: #5885c6;
	font-style:normal
}
.tyu{
	border: none;
}
.txt-h{
	width: 520px;
	overflow: hidden;
}
.tex-o{
	float: left;
	font-size: 14px;
	line-height: 80px;
	padding-right: 20px;
	color: #848484;
  height: 70px;
}

#glist {padding-bottom:25px; width: 120px;}
#glist span{
	float: left;
	padding-right: 10px;
  font-size: 14px;
  margin-top: 5px;
}
#glist a{
  float: right;
	padding: 5px 8px;
	color: #222222;
	font-size: 14px;
	border: #e3e3e3 solid 1px;
	display: block;
  width: 60px;
}
#glist a:hover{
	border: #f73a3a solid 1px;
	text-decoration: none;
	color: #f73a3a;
}
.gcIpt{
	height: 70px;
  text-align: left;
  padding-top: 15px;
}
.guT{
	color: #848484;
	font-size: 14px;
	padding-right:18px;
	line-height: 70px;
}
.gcIpt input{
	border: #e3e3e3 solid 1px;
	padding: 5px 8px;
	color: #848484;
	font-size: 16px;}
.nobdr-btns{
	padding-top: 10px;
  text-align: left;
}
.Hgt{ color: #424242; font-size:14px; padding-left: 10px;}
.addcart{
	background: #fd532d;
	padding: 0px 50px;
  border: 0;
	border-radius: 4px;
	color: #FFFFFF;
	margin-right: 10px;
	font-size:16px;
	line-height: 50px;
}
.yh{ background: #e60013;}
.addcart img{
  vertical-align:middle;
  margin-bottom:3px;
  padding-right: 5px;
}
.guarantee{
	height: 50px;
  text-align: left;
}
.guarantee span{
	color: #666666;
	font-size: 14px;
	line-height: 50px;
}

/* 商品评价 */
.gdetail{
	width:1240px;
	margin: 0 auto;
	margin-top: 20px;
	clear:both;
}
.ac-mod-list{
	width: 200px;
	margin: 0 auto;
	margin-bottom: 15px;
	text-align: center;
}
.ac-mod-list dt{
	padding: 5px;
}
.ac-mod-list dt img{
	width:180px;
	height: 155px;
}
.ac-mod-list dd{
	color: #424242;
	font-size: 14px;
}
.ac-mod-list dd span{
	display:block;
	color: #e31939;
	line-height: 2;
}
.detail{
	float:right;
	}
.sticky {
position: fixed;
top: 0;
} 

.active_tab{
	width:300px;
	margin:0 auto;
	margin-bottom: 20px;
	border-bottom:#e4393c solid 1px;
	height:37px;
	line-height:37px;
	background:#f7f7f7;	
}
.active_tab a{
	color:#666666;font-size: 14px;
	text-decoration:none;
}
.active_tab a:hover{
	color:#ffffff;
	text-decoration:none;
}
.act_title_left{
	float:left;
	width:100%;
  text-align:center;
  height:37px
}

.act_active{
	background:#e4393c;
	border-bottom:none !important;
}
.act_active a{color:#ffffff; font-size: 14px;}

.mui-ac{
	background: #e4393c none repeat scroll 0 0;
	
    float: left;
    font-size: 14px;
    height:25px;
    margin-top: 10px;
    line-height:25px;
    margin-left: 20px;
    padding: 0 8px;
}
.mui-ac a{color: #ffffff;}
.mui{
	float: left;margin-top:2px;
}
#mui-a{
	color: #666666;
}
#mui-a:hover{color: #666666;}

.active_list{
	width:300px;
	margin:0 auto;
}
.active_list a{text-decoration:none;}
#ui-a{
  width: 300px;
	height: 100%;
  color: #424242;
	font-size: 14px;
	line-height: 2;
  text-align: left;
	overflow: hidden;
  padding: 10px;
}

p,h1,h2,h3,h4,h5,h6,ul,dl,dt,form,input{
  margin:0;
  padding:0;
  border:0px;
}

ul{
  list-style:none;
}
a{
  text-decoration:none;
}

em{
  font-style:normal;
}

img{
  border:0px;
}

h1,h2,h3,h4,h5,h6{
  font-size:100%;
}
.clearfix:before,.clearfix:after{
  content:"";
  display:table;
}
.clearfix:after{
  clear:both;
}
.clearfix{
  zoom:1;
}


.fl{
  float:left;
}
.fr{
  float:right;
}
</style>


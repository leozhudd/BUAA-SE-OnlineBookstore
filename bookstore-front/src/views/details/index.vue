<template>
  <div id="details">
	<!-- 分割线 -->
	<div class="navbar_con"></div>
	<div class="submena clearfix">
		<router-link to="/">首页</router-link>
		<span>></span>
		<router-link to="/">{{book.book_category}}</router-link>
		<span>></span>
		<span>商品详情</span>
	</div>
	<div class="center_con clearfix">
		<div class="main_menu fl"><img :src="book.book_img"></div>
		<div class="goods_detail_list fr">
			<h3>{{book.book_name}}</h3>
            <h6>作者：<p @click="searchAuthor">{{book.book_author}}</p></h6> <h6>出版社：{{book.book_pub}}</h6>
			<p>{{book.book_intro}}</p>
			<div class="prize_bar">
				<div class="show_prize fl">￥<em>{{book.book_price}}</em></div>
				<div class="show_unit fl">
                  <td class="td-num">
                    <div class="product-num">
                      <a href="javascript:;" class="num-reduce num-do fl" @click='book.book_count--'>-</a>
                      <input type="text" class="num-input" v-model="book.book_count">
                      <a href="javascript:;" class="num-add num-do fr" @click='book.book_count++'>+</a>
                    </div>
                  </td>
                </div>
			</div>
			<div class="total">总价：<em>{{book.book_price * book.book_count}}</em></div>
			<div class="operate_btn">
				<button class="buy_btn" @click="orderIt">立即购买</button>
				<button class="add_cart" @click="addtoCart">加入购物车</button>
			</div>
		</div>
	</div>
  </div>
</template>

<script>
export default{
    name: "",
    data() {
        return {
            book: {
              'book_id':'1',
              'book_name':'csapp',
              'book_author':'Author',
              'book_price':39.00,
              'book_count':2,
              'book_img':'',
            }
        }
    },
    created() {
        //获取传入的参数
        book = this.$route.params;
    },
    methods:{
        orderIt() {
            let orderlist = [this.book];
            this.$router.push({name:'Order', params:{orderlist: orderlist}});
        },
        addtoCart() {
          let sendData = new FormData()
          sendData.append('book_id',this.book.book_id)
          sendData.append('book_count',this.book.book_count)
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
        searchAuthor() {
            this.$router.push({name: 'Search', params:{book_author: this.book.book_author} })
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

.guest_card{
	width:200px;
    height:40px;
    margin-top:34px;
}
.card_name{
	width:158px;
    height:38px;
    border:1px solid #ddd;
    font:14px/38px 'Microsoft YaHei UI';
    color:#37ab40;
    text-indent:56px;
    /* background:url(../images/icons.png) 10px -300px no-repeat #f7f7f7; */
}
.goods_count{
	width: 40px;
    height:40px;
    background-color:#f80;
    font:bold 18px/40px 'Microsoft YaHei UI';
    text-align:center;
    color:#fff;
}
.navbar_con{
	height:40px;
    border-bottom:2px solid #37ab30;
    /*background: red;*/
}
.navbar{
	width:1200px;
    height:40px;
    margin:0 auto;
    /*background: red;*/
}
.subnav_con h1{
	width:200px;
    height:40px;
    background-color: #37ab40;
    font:14px/40px 'Microsoft YaHei UI';
    text-align:center;
    color:#fff;
}
.subnav_con i{
	width: 11px;
	height: 7px;
	/* background:url(../images/down.png) left center no-repeat; */
	overflow: hidden;
	display: inline-block;
}
.navlist{
	overflow:hidden;
}
.navlist li{
	float:left;
    height:14px;
    padding:0 25px;
    border-left:1px solid #666;
    margin-left:-2px;
    margin-top:13px;
}
.submena{
    width: 1200px;
    height: 30px;
    margin: 0 auto;
    /*background:yellow;*/
}
.submena a{
    color:#37ab40;
    line-height: 30px;
}

.center_con{
	width: 1200px;
	height: 350px;
	margin: 0 auto;
	/*background: yellow;*/
}
.center_con .main_menu{
	width:350px;
    height:350px;
    overflow:hidden;
}
.goods_detail_list{
    width:730px;
    height:350px;
}
.goods_detail_list h3{
    font-size:24px;
    line-height:24px;
    color:#666;
    font-weight:normal;
}
.goods_detail_list p{
    color:#666;
    line-height:40px;
}
.prize_bar{
    height:72px;
    background-color:#fff5f5;
    line-height:72px;
}
.prize_bar .show_prize{
    font-size:20px;
    color:#ff3e3e;
    padding-left:20px
}
.prize_bar .show_pirze em{
    font-style:normal;
    font-size:36px;
    padding-left:10px
}
.prize_bar .show_unit{
    padding-left: 150px;
}
.goods_num{
    height: 52px;
    margin-top: 19px;
    /*background: yellow;*/
}
.goods_num .num_name{
    width:70px;
    height:52px;
    line-height:52px;
}
.goods_num .num_add{
    width:75px;
    height:50px;
    border:1px solid #dddddd;
}
.goods_num .num_add .num_show{
    width:49px;
    height:50px;
    text-align:center;
    line-height:50px;
    border:0px;
    outline:none;
    font-size:14px;
    color:#666;
}
.goods_num .num_add .add,.goods_num .num_add .minus{
    width:25px;
    line-height:25px;
    text-align:center;
    border-left:1px solid #ddd;
    border-bottom:1px solid #ddd;
    color:#666;
    font-size:14px;
}
.goods_num .num_add .minus{
    border-bottom:0px;
}
.total{
    height: 35px;
    line-height: 35px;
    margin-top: 25px;
    /*background: yellow;*/
}
.total em{
    font-style:normal;
    color:#ff3e3e;
    font-size:18px
}
.operate_btn{
    height:40px;
    margin-top:35px;
    font-size:0;
    position:relative;
}
.operate_btn .buy_btn,.operate_btn .add_cart{
    display:inline-block;
    width:178px;
    height:38px;
    border:1px solid #c40000;
    font-size:14px;
    color:#c40000;
    line-height:38px;
    text-align:center;
    background-color:#ffeded;
}
.operate_btn .add_cart{
    background-color:#c40000;
    color:#fff;
    margin-left:10px;
    position:relative;
    z-index:10;
}
.details .td-num{
      width:160px;
}
.product-num .num-do{
      width: 24px;
      height: 28px;
      background: #fff5f5;
      display: block;
}
.product-num .num-reduce a{
      display: inline;
      width: 6px;
      height: 2px;
      margin:13px auto 0 auto;
      
      /* background: url("cartBg.png") no-repeat -40px -22px; */
}
.product-num .num-add a{
      display: inline;
      width: 8px;
      height: 8px;
      margin:10px auto 0 auto;
      /* background: url("cartBg.png") no-repeat -60px -22px; */
}
.product-num .num-input{
      width: 42px;
      height: 28px;
      line-height:28px;
      border:none;
      text-align: center;
}

p,h1,h2,h3,h4,h5,h6,ul,dl,dt,form,input{
  margin:0;
  padding:0;
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


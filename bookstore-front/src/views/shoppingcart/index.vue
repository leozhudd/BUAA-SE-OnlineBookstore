<template>
    <div id="shopping-cart" class="page-shopping-cart">
        <h4 class="cart-title">购物车</h4>
        <!-- 标题 -->
        <div class="cart-product-title clearfix">
            <div class="td-check fl">
                <!-- 当切换到check-true类名时就调用全选函数 -->
                <button class="check-span fl check-all" :class="{'check-true':isSelectAll}"
                  @click="selectAll(isSelectAll)"></button>  <!-- 选择框 -->
                全选
            </div>
            <div class="td-product fl">商品</div>
            <div class="td-num fl">数量</div>
            <div class="td-price fl">单价(元)</div>
            <div class="td-total fl">金额(元)</div>
            <div class="td-do fl">操作</div>
        </div>
    
        <!-- 内容 -->
        <div v-if="!emptylist" class="cart-product clearfix">
          <table>
            <tbody>
              <tr v-for="(item, index) in BookList" :key="item.book_id">
                <td v-if="item.book_available" class="td-check">
                  <button @click="selectItem(item)" class="check-span" :class="{'check-true':item.select}"></button>选择
                </td>
                <td v-else class="td-check">
                  <button class="check-span"></button>库存不足
                </td>
                <td class="td-product">
                    <img :src="item.book_img" width="98" height="98" @click="toDetails(item)">
                    <div class="product-info">
                      <h6>{{item.book_name}}</h6>
                      <p>作者：{{item.book_author}}</p>
                    </div>
                    <div class="clearfix"></div>
                </td>
                <td class="td-num">
                    <div class="product-num">
                      <a href="javascript:;" class="num-reduce num-do fl" @click='countSub(item)'><span>-</span></a>
                      <input type="text" class="num-input" v-model="item.book_count">
                      <a href="javascript:;" class="num-add num-do fr" @click='countAdd(item)'><span>+</span></a>
                    </div>
                </td>
                <td class="td-price">
                  <p class="red-text"><span class="price-text">{{parseFloat(item.book_price) | showPrice}}</span></p>
                </td>
                <td class="td-total">
                  <p class="red-text"><span class="price-text">{{parseFloat(item.book_price)*item.book_count | showPrice}}</span></p>
                </td>
                <td class="td-do">
                  <button class="product-delete" @click='delBook(index,item)'>删除</button>
                </td>
              </tr>
    
            </tbody>
          </table>
        </div>
        <div v-else class="empty-list">您的购物车里没有商品，<router-link to="/">去选购</router-link></div>
        <router-view/>
    
        <!-- 最后一行统计 -->
        <div class="cart-product-info">
            <!-- <a href="javascript:;" class="delete-product" @click='deleteBooks'><span></span>删除所选商品</a> -->
            <a herf="javascript:;" class="keep-shopping" @click="this.$router.push('/')">继续购物</a>
            <a href="javascript:;" class="fr btn-buy" @click='orderBooks'>去结算</a>
            <a class="fr product-total"><span>{{getTotal.totalPrice | showPrice}}</span></a>
            <a class="fr check-num"><span>{{getTotal.totalNum}}</span>件商品总计（不含运费）:</a>
        </div>
    
        <!-- <div class="cart-worder clearfix">
           <a href="javascript:;" class="choose-worder fl"><span></span>绑定跟单员</a>
           <div class="worker-info fl">
           </div>
       </div> -->
    </div>
</template>

<script>
import {request} from "@/network/request.js";

    export default{
        name:'shoppingcart',
        data() {
          return {
            emptylist: false, 
            BookList:[
            {
              book_id:'1',
              book_name:'csapp',
              book_author:'Author',
              book_price:39.00,
              book_count:2,
              book_img:'',
              book_available:true
            },
            {
              book_id:'2',
              book_name:'csapp',
              book_author:'Author',
              book_price:39.00,
              book_count:2,
              book_img:'',
              book_available:false
            },
            {
              book_id:'3',
              book_name:'csapp',
              book_author:'Author',
              book_price:39.00,
              book_count:2,
              book_img:'',
              book_available:true
            }]
          }
        },

        created() {
          console.log(localStorage.getItem('isLogin'));
          if (this.$store.state.isLogin) {
            this.getBooks();
          }else{
            this.$message({
              type: "info",
              message: "请先登录",
            })
            this.$router.push('/login');
          }
        },
        computed:{
          // 检测是否全选
          isSelectAll() {
              //如果BookList中每一条数据的select都为true,就返回true,否则返回false
            for (let i in this.BookList) {
              if (this.BookList[i].book_available && !this.BookList[i].select)
                return false;
            }
            return true;
          },
    
        // 获取总价和产品总数
          getTotal() {
            let totalprice = 0, itemcount = 0;
            for (let i in this.BookList) {
              // 总价累加
              if (this.BookList[i].select) {
                totalprice += this.BookList[i].book_count * this.BookList[i].book_price;
                itemcount++;
              }
            }
            // 选择产品的件数，总价
            return{totalNum:itemcount, totalPrice:totalprice}
          }
    
        },
        filters: {
          showPrice(price) {
            if (!price) {
              return '';
            }
            return '￥' + price.toFixed(2);
          }
        },
        methods:{
          selectItem(item) {
            console.log(item.select);
            item.select=!item.select;
          },
          getBooks() {
            request({
              method: 'get',
              url: '/api/trade/show_shoppingcart/',
            }).then(res => {
              console.log(res);
              if (!res.error_num) {
                this.BookList = res.data;
                this.beSelectable();
                if (this.BookList.length === 0) {
                  this.emptylist = true;
                } else {
                  this.emptylist = false;
                }
                console.log(this.emptylist);
                console.log(this.BookList);
              } else {
                this.$message({
                  type: 'error',
                  message: '获取商品信息失败'+res.message
                });
              }
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
              this.$message({
                type: 'error',
                message: err.message
              });
            })
          },
          countAdd(item) {
            item.book_count++;
            this.updateCount(item);
          },
          countSub(item) {
            if (item.book_count>1){
                item.book_count--;
                this.updateCount(item);
            }
          },
          delBook(index, item) {
            alert("确定要删除吗？");
            let sendData = new FormData()
            sendData.append('book_id', item.book_id);
            request({
              method: 'post',
              url: '/api/trade/del_from_shoppingcart/',
              data: sendData
            }).then(res => {
              console.log(res);
              if (!res.error_num) {
              //在数组中删除 不行的话重新请求
                this.$message({
                  type: 'success',
                  message: '删除成功'
                })
                this.BookList.splice(index,1);
              } else {
                this.$message({
                  type: 'error',
                  message: res.message
                });
              }
            }).catch(err => {
              console.log(err);
              this.$message({
                type: 'error',
                message: '删除失败'
              });
            })
          },
          // 全选与取消全选
          selectAll(_isSelect){
            //遍历BookList,全部取反
            for (let i in this.BookList) {
              if (this.BookList[i].book_available)
                this.BookList[i].select = !_isSelect;
            }
          },
          //下单选中的产品
          orderBooks(){
            let orderlist = [];
            for (let i in this.BookList) {
              if (this.BookList[i].select) {
                orderlist.push(this.BookList[i]);
              }
            }
            this.$router.push({path:'/order', query:{comefrom:'cart',orderlist: JSON.stringify(orderlist)}});
          },
          toDetails(item) {
            //发送id，在详情页加载信息
            this.$router.push({path: '/details', query: {book_id: item.book_id}});
          },
          beSelectable() {
          //为BookList添加select属性（是否选中字段）默认为false
          let _this=this;
          for (let i in this.BookList) {
              _this.$set(this.BookList[i],'select',false);
            }
          }

        },
    }
</script>

<style>
    .fl{
      float: left;
    }
    .fr{
      float: right;
    }
    blockquote, body, dd, div, dl, dt, fieldset, form, h1, h2, h3, h4, h5, h6, img, input, li, ol, p, table, td, textarea, th, ul {
      margin: 0;
      padding: 0;
    }
    .clearfix{
      zoom: 1;
    }
    .clearfix:after {
      clear: both;
    }
    .clearfix:after {
      content: '.';
      display: block;
      overflow: hidden;
      visibility: hidden;
      font-size: 0;
      line-height: 0;
      width: 0;
      height: 0;
    }
    a{
      text-decoration: none;
      color: #333;
    }
    img{vertical-align: middle;}
    .page-shopping-cart{
      width: 1200px;
      margin:40px auto;
      font-size: 14px;
      border:1px solid #e3e3e3;
      border-top:1px solid #42b983;
    }
    .page-shopping-cart .cart-title{
      color:#42b983;
      font-size: 16px;
      text-align: left;
      padding-left: 20px;
      line-height: 68px;
    }
    .page-shopping-cart .red-text {
      color: #e94826;
    }
    .page-shopping-cart .check-span{
      display: block;
      width: 20px;
      height: 20px;
      margin-top: 9px;
      border-radius: 20px;
      border: 1px solid #666;
    }
    
    /* 点击时改变勾选 */
    .check-true{
      background-color: #3ad68e;
    } 
    .page-shopping-cart .td-check{
      width:70px;
      text-align: left;
    }
    .page-shopping-cart .td-product{
      width:460px;
    }
    .page-shopping-cart .td-num, .page-shopping-cart .td-price, .page-shopping-cart .td-total{
      width:160px;
    }
    .page-shopping-cart .td-do{
      width:150px;
    }
    .cart-product-title{
      text-align: center;
      height: 38px;
      line-height: 38px;
      padding: 0 20px;
      background-color: #f7f7f7;
      border-top: 1px solid #e3e3e3;
      border-bottom: 1px solid #e3e3e3;
    }
    .cart-product-title .td-product{
      text-align: center;
      font-size: 14px;
    }
    .cart-product-title .td-check{
      text-align: left;
    }
    .cart-product-title .td-check .check-span .check-span{
      margin:9px 6px 0 0;
    }
    
    /* 内容开始 */
    .cart-product{
      padding: 0 20px;
      text-align: center;
    }
    .cart-product table{
      width: 100%;
      text-align: center;
      font-size: 14px;
    }
    .cart-product table td{
      padding: 20px 0;
    }
    .cart-product table tr{
      border-bottom:1px dashed #e3e3e3;
    }
    .cart-product table tr:last-child{
      border-bottom:none;
    }
    .cart-product table .product-num{
      border: 1px solid #e3e3e3;
      display: inline-block;
      text-align: center;
    }
    .cart-product table .product-num .num-do{
      width: 24px;
      height: 28px;
      background: #f7f7f7;
      display: block;
    }
    .cart-product table .product-num .num-reduce span{
      display: block;
      width: 6px;
      height: 2px;
      margin:13px auto 0 auto;
      /* background: url("cartBg.png") no-repeat -40px -22px; */
    }
    .cart-product table .product-num .num-add span{
      display: block;
      width: 8px;
      height: 8px;
      margin:10px auto 0 auto;
      /* background: url("cartBg.png") no-repeat -60px -22px; */
    }
    .cart-product table .product-num .num-input{
      width: 42px;
      height: 28px;
      line-height:28px;
      border:none;
      text-align: center;
    }
    .cart-product table .td-product{
      text-align: center;
      font-size: 12px;
      line-height: 20px;
    }
    .cart-product table .td-product img{
      border:1px solid #e3e3e3;
      margin-right: 10px;
    }
    .cart-product table .td-product .product-info{
      display: inline-block;
      vertical-align: middle;
      text-align: left;
    }
    .cart-product table .td-do{
      font-size: 12px;
    }
    
    /* 最后一行统计 */
    
    .cart-product-info{
      height:50px;
      line-height: 50px;
      background: #f7f7f7;
      padding-left: 20px;
    }
    .cart-product-info .delete-product{
      color:#666;
    }
    .cart-product-info .delete-product span{
      display: inline-block;
      vertical-align: top;
      margin:18px 8px 0 0;
      width:13px;
      height: 15px;
      /* background: url("cartBg.png") no-repeat -60px 0; */
    }
    .cart-product-info .product-total{
      font-size: 14px;
      color:#e94826;
    }
    .cart-product-info .product-total span{
      font-size: 20px;
    }
    .cart-product-info .check-num{
      color:#333;
    }
    .cart-product-info .check-num span{
      color: #e94826;
    }
    .cart-product-info .keep-shopping{
      color: #666;
      margin-left: 40px;
    }
    .cart-product-info .keep-shopping span{
      display: inline-block;
      vertical-align: top;
      margin:18px 8px 0 0;
      width: 15px;
      height: 15px;
      /* background: url("cartBg.png") no-repeat -40px 0; */
    }
    .cart-product-info .btn-buy{
      height: 50px;
      color: #fff;
      font-size: 20px;
      display: block;
      width: 110px;
      background: #ff7700;
      text-align: center;
      margin-left: 30px;
    }
    
    
    
    /* cart-worder */
    
    .page-shopping-cart .cart-worder {
        padding: 20px; }
    .page-shopping-cart .cart-worder .choose-worder {
        color: #fff;
        display: block;
        background: #39e;
        width: 140px;
        height: 40px;
        line-height: 40px;
        border-radius: 4px;
        text-align: center;
        margin-right: 20px; }
    .page-shopping-cart .cart-worder .choose-worder span {
        display: inline-block;
        vertical-align: top;
        margin: 9px 10px 0 0;
        width: 22px;
        height: 22px;
        /* background: url("cartBg.png") no-repeat -92px 0; */
    } 
    .page-shopping-cart .cart-worder .worker-info {
        color: #666; }
    .page-shopping-cart .cart-worder .worker-info img {
        border-radius: 100%;
        margin-right: 10px; }
    .page-shopping-cart .cart-worder .worker-info span {
        color: #000; }
    
    .choose-worker-box {
        width: 620px;
        background: #fff; }
    .choose-worker-box .box-title {
        height: 40px;
        line-height: 40px;
        background: #F7F7F7;
        text-align: center;
        position: relative;
        font-size: 14px; }
    .choose-worker-box .box-title a {
        display: block;
        position: absolute;
        top: 15px;
        right: 16px;
        width: 10px;
        height: 10px;
        /*background: url("shopping_cart.png") no-repeat -80px 0; */}
    /*.choose-worker-box .box-title a:hover {
        background: url("shopping_cart.png") no-repeat -80px -22px; }*/
    .choose-worker-box .worker-list {
        padding-top: 30px;
        height: 134px;
        overflow-y: auto; }
    .choose-worker-box .worker-list li {
        float: left;
        width: 25%;
        text-align: center;
        margin-bottom: 30px; }
    .choose-worker-box .worker-list li p {
        margin-top: 8px; }
    .choose-worker-box .worker-list li.cur a {
        color: #f70; }
    .choose-worker-box .worker-list li.cur a img {
        border: 1px solid #f70; }
    .choose-worker-box .worker-list li a:hover {
        color: #f70; }
    .choose-worker-box .worker-list li a:hover img {
        border: 1px solid #f70; }
    .choose-worker-box .worker-list li img {
        border: 1px solid #fff;
        border-radius: 100%; }
</style>
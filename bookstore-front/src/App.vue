<template>
  <div id="app">
    <div id="SiteNav" class="site-nav">
	    <div id="SiteNavBd" class="site-nav-bd">
		    <ul id="SiteNavBdL" class="site-nav-bd-l">
			    <li id="LoginInfo" class="menu">
				    <div class="menu-hd" v-if="!isLogin"><router-link to ="/login">登录/注册</router-link></div>
            <div v-else>{{user_name}} | <a herf="javascript:;" @click="Logout">注销</a></div>  
			    </li>
          <li class="menu">
            <div class="menu-hd">
					    <router-link to ="/chgps">修改密码</router-link>
				    </div>  
          </li>
		    </ul>
		    <ul id="SiteNavBdR" class="site-nav-bd-r">
          <li class="menu home">
            <div class="menu-hd">
					    <router-link to ="/">书店首页</router-link>
				    </div>  
          </li>
          <li class="menu">
            <div class="menu-hd">
					    <router-link to ="/shoppingcart">购物车</router-link>
				    </div>  
          </li>
          <li class="menu">
            <div class="menu-hd">
					    <router-link to ="/myorders">我的订单</router-link>
				    </div>  
          </li>
          <li class="menu">
            <div class="menu-hd">
					    <router-link to ="/myorders">个人中心</router-link>
				    </div>  
          </li>
          <li class="menu">
            <div class="menu-hd">
					    <router-link to ="/order">订单</router-link>
				    </div>  
          </li>
          <li class="menu">
            <div class="menu-hd">
					    <router-link to ="/details">详情</router-link>
				    </div>  
          </li>
		    </ul>
	    </div>
	  </div>	
    <div class="search_bar clearfix">
		  <a href="#" class="logo fl"><img src=""></a>
		  <div class="search_con fl">
        <select class="input_select fl" v-model="searchkey" @change="selectKey($event)">
          <option value="bookname">书名</option>
          <option value="author">作者</option>
          <option value="publisher">出版社</option>
        </select>
			  <input type="text" class="input_text fl" placeholder="输入关键字搜索商品" v-model="keyword">
			  <button class="input_btn fr" @click="searchIndexOf">搜索</button>
		  </div>
	  </div>
    <!-- 分割线 -->
    <div class="navbar_con"></div>
    <router-view></router-view>
  </div>
</template>

<script>
import {request} from "@/network/request.js";
export default {
  name:'Head',
  data() {
    return {
      user_name: localStorage.getItem("username"),
      isLogin: localStorage.getItem("isLogin"),
      searchkey: 'bookname',
      keyword: '',
      bookname: '',
      author: '',
      publisher: ''
    }
  },
  methods: {
    searchIndexOf() {
      if (this.searchkey === 'bookname'){
        this.bookname = this.keyword;
      } else if(this.searchkey === 'author') {
        this.author = this.keyword;
      } else if(this.searchkey === 'publisher') {
        this.publisher = this.keyword;
      }
      console.log(this.keyword);
      let sendData = new FormData()
      sendData.append('option', this.searchkey)
      sendData.append('bookname', this.bookname)
      sendData.append('author', this.author)
      sendData.append('publisher', this.publisher)

      request({
          method: 'post',
          url: '/api/base/keywords_search/',
          data: sendData
        }).then(res => {
          console.log(res);
          if (!res.error_num) {
            let resultlist = JSON.stringify(res.data);
            this.$router.push({
              path:'/srchresult',
              query:{
                resultlist: resultlist
              }
            })
          }
        }).catch(err => {
          console.log(err);
      })
    },

    selectKey(event){
      this.searchkey = event.target.value; //获取option对应的value值
    },
    Logout() {
      request({
        method: 'get',
        url: '/api/base/logout/'
      }).then(res => {
        if(!res.error_num){
          localStorage.setItem("username",'');
          this.$store.commit('logout');
          this.$message({
            type: 'info',
            message: '注销成功'
          });
          this.$router.push('/login');
        }else {
          this.$message({
            type: 'error',
            message: '注销失败'+res.message
          });
        }
      }).catch(err => {
        this.$message({
          type: 'error',
          message: '注销失败'+err.message
        })
      })
    }
  }
}
</script>

<style>
div {
		display: block;
	}
.navbar_con{
	height:40px;
    border-bottom:2px solid #37ab30;
    /*background: red;*/
}
.site-nav{
		z-index: 1000;
		width: 100%;
		background:#f5f5f5;
		border-bottom: 1px solid #eee;
}
.site-nav .site-nav-bd{
		margin: 0 auto;
		width: 990px;
		height: 35px;
		background:#f5f5f5;
}
.site-nav .site-nav-bd .site-nav-bd-l, .site-nav .site-nav-bd .site-nav-bd-l .menu{
		float: left;
}
  .site-nav .site-nav-bd .site-nav-bd-r .menu {
    float: right;
  }
	.site-nav-bd .menu .menu-hd {
    	z-index: 10002;
    	position: relative;
    	padding: 0 6px;
    	height: 35px;
   		line-height: 35px;
	}
.menu-hd .router-link-exact-active {
  color: #42b983;
}

.search_bar{
	width:1200px;
    height:115px;
    margin:0 auto;
}
.logo{
	width:151px;
    height:59px;
    margin:29px 0 0 17px;
}
.search_con{
	width:660px;
    height:38px;
    border:1px solid #37ab40;
    margin:34px 0 0 123px;
    /* background:url(../images/icons.png) 10px -335px no-repeat; */
}
.search_con .input_text{
    width:463px;
    height:37px;
    border:0px;
    margin-left:27px;
    outline:none;
}
.search_con .input_btn{
    width:90px;
    height:39px;
    background-color: #37ab40;
    border:0;
    font:14px/38px 'Microsoft YaHei UI';
    color:#fff;
    /*鼠标变成手*/
    cursor:pointer;
}
.input_select {
  height:39px;
  width:80px;
  font-size:14px;
  border:1px solid #37ab40;
}

#app {
  text-align: center;
  color: #2c3e50;
}
blockquote, dd, div, dl, dt, fieldset, form, h1, h2, h3, h4, h5, h6, img, input, li, ol, p, table, td, textarea, th, ul {
  margin: 0;
  padding: 0;
}
.fl{
  float: left;
}
.fr{
  float: right;
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
ul{
  list-style:none;
}

a{ text-decoration:none;  color: #666;}
a:hover{ text-decoration:none; color:#46b448;} 
em{
  font-style:normal;
}

img{
  border:0px;
}

h1,h2,h3,h4,h5,h6{
  font-size:100%;
}
</style>

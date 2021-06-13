<template>
  <div id="app">
    <div id="SiteNav" class="site-nav">
	    <div id="SiteNavBd" class="site-nav-bd">
		    <ul id="SiteNavBdL" class="site-nav-bd-l">
			    <li id="LoginInfo" class="menu">
				    <div class="menu-hd" v-if="!this.$store.state.isLogin"><router-link to ="/login">登录/注册</router-link></div>
            <div v-else>{{user_name}}</div>  
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
					    <router-link to ="/chgpass">个人中心</router-link>
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
			  <input type="text" class="input_text fl" placeholder="输入关键字搜索商品">
			  <button class="input_btn fr" @click="searchIndexOf">搜索</button>
		  </div>
	  </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name:'Head',
  data() {
    return {
      user_name: localStorage.getItem("username"),
    }
  },
  methods: {
    searchIndexOf() {

    }
  }
}
</script>

<style>
div {
		display: block;
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
	width:616px;
    height:38px;
    border:1px solid #37ab40;
    margin:34px 0 0 123px;
    /* background:url(../images/icons.png) 10px -335px no-repeat; */
}
.search_con .input_text{
    width:470px;
    height:37px;
    border:0px;
    margin-left:37px;
    outline:none;
}
.search_con .input_btn{
    width:100px;
    height:38px;
    background-color: #37ab40;
    border:0;
    font:14px/38px 'Microsoft YaHei UI';
    color:#fff;
    /*鼠标变成手*/
    cursor:pointer;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#menu-right {
  padding-right: 24px;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

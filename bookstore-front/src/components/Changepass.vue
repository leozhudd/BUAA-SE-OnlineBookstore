<template>
  <div id="chgps">
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
        <div>输入旧密码:<input v-model="oldpass"></div>
        <div>输入新密码:<input v-model="newpass1"></div>
        <div>确认新密码:<input v-model="newpass2"></div>
        <button @click="submitChange">确认修改</button>
      </div>
    </div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";

export default{
  name:'Changepass',
  data() {
    return {
      oldpass: '',
      newpass1: '',
      newpass2: '',
    }
  },
  methods:{
    submitChange() {
      let sendData = new FormData()
      sendData.append('password',this.oldpass)
      sendData.append('new_password', this.newpass2)

          request({
            method: 'post',
            url: '/api/base/chg_pw/',
            data: sendData
          })
          .then(res => {
            if(!res.error_num)
            {
              this.$message({
                type: 'success',
                message: '修改成功'
              });
              this.$router.go(0);
            }
            else
            {
              this.$message({
                type: 'error',
                message: res.message,
              });
            }
          }).catch(error=>{
            this.$message({
              type: 'error',
              message: '修改失败'+error.message
            });
          });
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

.help-r{
	border: 1px solid #ddd;
	width: 980px;
  margin-top: 40px;
}
</style>
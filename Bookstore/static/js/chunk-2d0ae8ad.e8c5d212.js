(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0ae8ad"],{"0b05":function(e,s,a){"use strict";a.r(s);var n=function(){var e=this,s=e.$createElement,a=e._self._c||s;return a("div",[a("div",[e._v("输入旧密码:"),a("input",{directives:[{name:"model",rawName:"v-model",value:e.oldpass,expression:"oldpass"}],domProps:{value:e.oldpass},on:{input:function(s){s.target.composing||(e.oldpass=s.target.value)}}})]),a("div",[e._v("输入新密码:"),a("input",{directives:[{name:"model",rawName:"v-model",value:e.newpass1,expression:"newpass1"}],domProps:{value:e.newpass1},on:{input:function(s){s.target.composing||(e.newpass1=s.target.value)}}})]),a("div",[e._v("确认新密码:"),a("input",{directives:[{name:"model",rawName:"v-model",value:e.newpass2,expression:"newpass2"}],domProps:{value:e.newpass2},on:{input:function(s){s.target.composing||(e.newpass2=s.target.value)}}})]),a("button",{on:{click:e.submitChange}},[e._v("确认修改")])])},t=[],o=a("1bab"),p={name:"Changepass",data:function(){return{oldpass:"",newpass1:"",newpass2:""}},methods:{submitChange:function(){var e=this,s=new FormData;s.append("password",this.oldpass),s.append("new_password",this.newpass2),Object(o["a"])({method:"post",url:"/api/base/chg_pw/",data:s}).then((function(s){s.error_num?e.$message({type:"error",message:s.message}):(e.$message({type:"success",message:"修改成功"}),e.$router.go(0))})).catch((function(s){e.$message({type:"error",message:"修改失败"+s.message})}))}}},r=p,i=a("2877"),u=Object(i["a"])(r,n,t,!1,null,null,null);s["default"]=u.exports}}]);
//# sourceMappingURL=chunk-2d0ae8ad.e8c5d212.js.map
(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1b06708a"],{1148:function(t,e,o){"use strict";var n=o("a691"),r=o("1d80");t.exports=function(t){var e=String(r(this)),o="",a=n(t);if(a<0||a==1/0)throw RangeError("Wrong number of repetitions");for(;a>0;(a>>>=1)&&(e+=e))1&a&&(o+=e);return o}},"408a":function(t,e,o){var n=o("c6b6");t.exports=function(t){if("number"!=typeof t&&"Number"!=n(t))throw TypeError("Incorrect invocation");return+t}},"634a":function(t,e,o){"use strict";o.r(e);var n=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{attrs:{id:"order"}},[o("table",[o("tbody",t._l(t.books,(function(e){return o("tr",{key:e.book_id},[o("td",{staticClass:"td-product"},[o("img",{attrs:{src:e.book_img,width:"98",height:"98"}}),o("div",{staticClass:"product-info"},[o("h6",[t._v(t._s(e.book_name))]),o("p",[t._v("作者："+t._s(e.book_author))])]),o("div",{staticClass:"clearfix"})]),o("td",{staticClass:"td-num"},[t._v(" 单价："),o("div",[t._v(t._s(t._f("showPrice")(parseFloat(e.book_price))))])]),o("td",{staticClass:"td-count"},[t._v(" 数量："),o("div",[t._v(t._s(e.book_count))])])])})),0)]),o("div",[t._v(" 收件人姓名："),o("input",{directives:[{name:"model",rawName:"v-model",value:t.contact_name,expression:"contact_name"}],domProps:{value:t.contact_name},on:{input:function(e){e.target.composing||(t.contact_name=e.target.value)}}}),t._v(" 电话："),o("input",{directives:[{name:"model",rawName:"v-model",value:t.contact_phone,expression:"contact_phone"}],domProps:{value:t.contact_phone},on:{input:function(e){e.target.composing||(t.contact_phone=e.target.value)}}}),t._v(" 收货地址："),o("input",{directives:[{name:"model",rawName:"v-model",value:t.address,expression:"address"}],domProps:{value:t.address},on:{input:function(e){e.target.composing||(t.address=e.target.value)}}}),t._v(" 备注："),o("input",{directives:[{name:"model",rawName:"v-model",value:t.memo,expression:"memo"}],domProps:{value:t.memo},on:{input:function(e){e.target.composing||(t.memo=e.target.value)}}}),o("span",[t._v("总金额："+t._s(t.totalPrice))])]),o("div",[o("button",{on:{click:t.cancelOrder}},[t._v("取消订单")]),o("button",{on:{click:t.submitOrder}},[t._v("提交订单")])])])},r=[],a=(o("b680"),o("1bab")),i={name:"Order",data:function(){return{books:[],memo:"",address:"",contact_name:"",contact_phone:"",totalPrice:0}},created:function(){this.books=JSON.parse(this.$route.query.orderlist)},filters:{showPrice:function(t){return t?"￥"+t.toFixed(2):""}},computed:{getTotal:function(){var t=0;for(var e in this.books)t+=this.books[e].count*this.book[e].price;this.totalPrice=t}},methods:{submitOrder:function(){var t=this,e=[];for(var o in this.books)e.push(this.books[o].book_id);console.log(e);var n=new FormData;n.append("book_list",JSON.stringify(e)),n.append("memo",this.memo),n.append("address",this.address),n.append("contact_name",this.contact_name),n.append("contact_phone",this.contact_phone),Object(a["a"])({method:"post",url:"/api/trade/creat_new_order/",traditional:!0,data:n}).then((function(e){console.log(e),e.error_num?t.$message({type:"error",message:"订单提交失败"+e.message}):t.$message({type:"success",message:"订单提交成功"})})).catch((function(e){console.log(e),t.$message({type:"error",message:"订单提交失败"})}))},cancelOrder:function(){this.$router.go(-1)}}},s=i,c=o("2877"),u=Object(c["a"])(s,n,r,!1,null,null,null);e["default"]=u.exports},b680:function(t,e,o){"use strict";var n=o("23e7"),r=o("a691"),a=o("408a"),i=o("1148"),s=o("d039"),c=1..toFixed,u=Math.floor,d=function(t,e,o){return 0===e?o:e%2===1?d(t,e-1,o*t):d(t*t,e/2,o)},l=function(t){var e=0,o=t;while(o>=4096)e+=12,o/=4096;while(o>=2)e+=1,o/=2;return e},m=function(t,e,o){var n=-1,r=o;while(++n<6)r+=e*t[n],t[n]=r%1e7,r=u(r/1e7)},p=function(t,e){var o=6,n=0;while(--o>=0)n+=t[o],t[o]=u(n/e),n=n%e*1e7},v=function(t){var e=6,o="";while(--e>=0)if(""!==o||0===e||0!==t[e]){var n=String(t[e]);o=""===o?n:o+i.call("0",7-n.length)+n}return o},h=c&&("0.000"!==8e-5.toFixed(3)||"1"!==.9.toFixed(0)||"1.25"!==1.255.toFixed(2)||"1000000000000000128"!==(0xde0b6b3a7640080).toFixed(0))||!s((function(){c.call({})}));n({target:"Number",proto:!0,forced:h},{toFixed:function(t){var e,o,n,s,c=a(this),u=r(t),h=[0,0,0,0,0,0],f="",_="0";if(u<0||u>20)throw RangeError("Incorrect fraction digits");if(c!=c)return"NaN";if(c<=-1e21||c>=1e21)return String(c);if(c<0&&(f="-",c=-c),c>1e-21)if(e=l(c*d(2,69,1))-69,o=e<0?c*d(2,-e,1):c/d(2,e,1),o*=4503599627370496,e=52-e,e>0){m(h,0,o),n=u;while(n>=7)m(h,1e7,0),n-=7;m(h,d(10,n,1),0),n=e-1;while(n>=23)p(h,1<<23),n-=23;p(h,1<<n),m(h,1,1),p(h,2),_=v(h)}else m(h,0,o),m(h,1<<-e,0),_=v(h)+i.call("0",u);return u>0?(s=_.length,_=f+(s<=u?"0."+i.call("0",u-s)+_:_.slice(0,s-u)+"."+_.slice(s-u))):_=f+_,_}})}}]);
//# sourceMappingURL=chunk-1b06708a.8aceaff9.js.map
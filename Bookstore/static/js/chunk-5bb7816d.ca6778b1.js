(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5bb7816d"],{"057f":function(t,o,e){var r=e("fc6a"),n=e("241c").f,i={}.toString,a="object"==typeof window&&window&&Object.getOwnPropertyNames?Object.getOwnPropertyNames(window):[],s=function(t){try{return n(t)}catch(o){return a.slice()}};t.exports.f=function(t){return a&&"[object Window]"==i.call(t)?s(t):n(r(t))}},"65f0":function(t,o,e){var r=e("861d"),n=e("e8b5"),i=e("b622"),a=i("species");t.exports=function(t,o){var e;return n(t)&&(e=t.constructor,"function"!=typeof e||e!==Array&&!n(e.prototype)?r(e)&&(e=e[a],null===e&&(e=void 0)):e=void 0),new(void 0===e?Array:e)(0===o?0:o)}},"746f":function(t,o,e){var r=e("428f"),n=e("5135"),i=e("e538"),a=e("9bf2").f;t.exports=function(t){var o=r.Symbol||(r.Symbol={});n(o,t)||a(o,t,{value:i.f(t)})}},"89a4":function(t,o,e){"use strict";e("b61a")},a4d3:function(t,o,e){"use strict";var r=e("23e7"),n=e("da84"),i=e("d066"),a=e("c430"),s=e("83ab"),c=e("4930"),u=e("fdbf"),f=e("d039"),l=e("5135"),b=e("e8b5"),d=e("861d"),p=e("825a"),h=e("7b0b"),v=e("fc6a"),m=e("c04e"),g=e("5c6c"),y=e("7c73"),k=e("df75"),_=e("241c"),w=e("057f"),S=e("7418"),O=e("06cf"),C=e("9bf2"),j=e("d1e7"),$=e("9112"),x=e("6eeb"),P=e("5692"),A=e("f772"),N=e("d012"),E=e("90e3"),F=e("b622"),J=e("e538"),I=e("746f"),T=e("d44e"),q=e("69f3"),z=e("b727").forEach,D=A("hidden"),B="Symbol",Q="prototype",W=F("toPrimitive"),G=q.set,H=q.getterFor(B),K=Object[Q],L=n.Symbol,M=i("JSON","stringify"),R=O.f,U=C.f,V=w.f,X=j.f,Y=P("symbols"),Z=P("op-symbols"),tt=P("string-to-symbol-registry"),ot=P("symbol-to-string-registry"),et=P("wks"),rt=n.QObject,nt=!rt||!rt[Q]||!rt[Q].findChild,it=s&&f((function(){return 7!=y(U({},"a",{get:function(){return U(this,"a",{value:7}).a}})).a}))?function(t,o,e){var r=R(K,o);r&&delete K[o],U(t,o,e),r&&t!==K&&U(K,o,r)}:U,at=function(t,o){var e=Y[t]=y(L[Q]);return G(e,{type:B,tag:t,description:o}),s||(e.description=o),e},st=u?function(t){return"symbol"==typeof t}:function(t){return Object(t)instanceof L},ct=function(t,o,e){t===K&&ct(Z,o,e),p(t);var r=m(o,!0);return p(e),l(Y,r)?(e.enumerable?(l(t,D)&&t[D][r]&&(t[D][r]=!1),e=y(e,{enumerable:g(0,!1)})):(l(t,D)||U(t,D,g(1,{})),t[D][r]=!0),it(t,r,e)):U(t,r,e)},ut=function(t,o){p(t);var e=v(o),r=k(e).concat(pt(e));return z(r,(function(o){s&&!lt.call(e,o)||ct(t,o,e[o])})),t},ft=function(t,o){return void 0===o?y(t):ut(y(t),o)},lt=function(t){var o=m(t,!0),e=X.call(this,o);return!(this===K&&l(Y,o)&&!l(Z,o))&&(!(e||!l(this,o)||!l(Y,o)||l(this,D)&&this[D][o])||e)},bt=function(t,o){var e=v(t),r=m(o,!0);if(e!==K||!l(Y,r)||l(Z,r)){var n=R(e,r);return!n||!l(Y,r)||l(e,D)&&e[D][r]||(n.enumerable=!0),n}},dt=function(t){var o=V(v(t)),e=[];return z(o,(function(t){l(Y,t)||l(N,t)||e.push(t)})),e},pt=function(t){var o=t===K,e=V(o?Z:v(t)),r=[];return z(e,(function(t){!l(Y,t)||o&&!l(K,t)||r.push(Y[t])})),r};if(c||(L=function(){if(this instanceof L)throw TypeError("Symbol is not a constructor");var t=arguments.length&&void 0!==arguments[0]?String(arguments[0]):void 0,o=E(t),e=function(t){this===K&&e.call(Z,t),l(this,D)&&l(this[D],o)&&(this[D][o]=!1),it(this,o,g(1,t))};return s&&nt&&it(K,o,{configurable:!0,set:e}),at(o,t)},x(L[Q],"toString",(function(){return H(this).tag})),x(L,"withoutSetter",(function(t){return at(E(t),t)})),j.f=lt,C.f=ct,O.f=bt,_.f=w.f=dt,S.f=pt,J.f=function(t){return at(F(t),t)},s&&(U(L[Q],"description",{configurable:!0,get:function(){return H(this).description}}),a||x(K,"propertyIsEnumerable",lt,{unsafe:!0}))),r({global:!0,wrap:!0,forced:!c,sham:!c},{Symbol:L}),z(k(et),(function(t){I(t)})),r({target:B,stat:!0,forced:!c},{for:function(t){var o=String(t);if(l(tt,o))return tt[o];var e=L(o);return tt[o]=e,ot[e]=o,e},keyFor:function(t){if(!st(t))throw TypeError(t+" is not a symbol");if(l(ot,t))return ot[t]},useSetter:function(){nt=!0},useSimple:function(){nt=!1}}),r({target:"Object",stat:!0,forced:!c,sham:!s},{create:ft,defineProperty:ct,defineProperties:ut,getOwnPropertyDescriptor:bt}),r({target:"Object",stat:!0,forced:!c},{getOwnPropertyNames:dt,getOwnPropertySymbols:pt}),r({target:"Object",stat:!0,forced:f((function(){S.f(1)}))},{getOwnPropertySymbols:function(t){return S.f(h(t))}}),M){var ht=!c||f((function(){var t=L();return"[null]"!=M([t])||"{}"!=M({a:t})||"{}"!=M(Object(t))}));r({target:"JSON",stat:!0,forced:ht},{stringify:function(t,o,e){var r,n=[t],i=1;while(arguments.length>i)n.push(arguments[i++]);if(r=o,(d(o)||void 0!==t)&&!st(t))return b(o)||(o=function(t,o){if("function"==typeof r&&(o=r.call(this,t,o)),!st(o))return o}),n[1]=o,M.apply(null,n)}})}L[Q][W]||$(L[Q],W,L[Q].valueOf),T(L,B),N[D]=!0},b0c0:function(t,o,e){var r=e("83ab"),n=e("9bf2").f,i=Function.prototype,a=i.toString,s=/^\s*function ([^ (]*)/,c="name";r&&!(c in i)&&n(i,c,{configurable:!0,get:function(){try{return a.call(this).match(s)[1]}catch(t){return""}}})},b61a:function(t,o,e){},b727:function(t,o,e){var r=e("0366"),n=e("44ad"),i=e("7b0b"),a=e("50c4"),s=e("65f0"),c=[].push,u=function(t){var o=1==t,e=2==t,u=3==t,f=4==t,l=6==t,b=7==t,d=5==t||l;return function(p,h,v,m){for(var g,y,k=i(p),_=n(k),w=r(h,v,3),S=a(_.length),O=0,C=m||s,j=o?C(p,S):e||b?C(p,0):void 0;S>O;O++)if((d||O in _)&&(g=_[O],y=w(g,O,k),t))if(o)j[O]=y;else if(y)switch(t){case 3:return!0;case 5:return g;case 6:return O;case 2:c.call(j,g)}else switch(t){case 4:return!1;case 7:c.call(j,g)}return l?-1:u||f?f:j}};t.exports={forEach:u(0),map:u(1),filter:u(2),some:u(3),every:u(4),find:u(5),findIndex:u(6),filterOut:u(7)}},cfeb:function(t,o,e){"use strict";e.r(o);var r=function(){var t=this,o=t.$createElement,e=t._self._c||o;return e("div",{attrs:{id:"details"}},[e("div",{staticClass:"submena clearfix"},[e("router-link",{attrs:{to:"/"}},[t._v("首页")]),e("span",[t._v(">")]),e("router-link",{attrs:{to:"/"}},[t._v(t._s(t.book.category))]),e("span",[t._v(">")]),e("span",[t._v("商品详情")])],1),e("div",{staticClass:"center_con clearfix"},[e("div",{staticClass:"main_menu fl"},[e("img",{attrs:{src:t.book.image}})]),e("div",{staticClass:"goods_detail_list fr"},[e("h3",[t._v(t._s(t.book.name))]),e("h6",[t._v("作者："),e("a",{on:{click:t.searchAuthor}},[t._v(t._s(t.book.author))])]),t._v(" "),e("h6",[t._v("出版社："+t._s(t.book.publisher))]),e("p",[t._v(t._s(t.book.description))]),e("div",{staticClass:"prize_bar"},[e("div",{staticClass:"show_prize fl"},[t._v("￥"),e("em",[t._v(t._s(t.book.price))])]),e("div",{staticClass:"show_unit fl"},[e("td",{staticClass:"td-num"},[e("div",{staticClass:"product-num"},[e("a",{staticClass:"num-reduce num-do fl",attrs:{href:"javascript:;"},on:{click:t.countSub}},[t._v("-")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.book.count,expression:"book.count"}],staticClass:"num-input",attrs:{type:"text"},domProps:{value:t.book.count},on:{input:function(o){o.target.composing||t.$set(t.book,"count",o.target.value)}}}),e("a",{staticClass:"num-add num-do fr",attrs:{href:"javascript:;"},on:{click:t.countAdd}},[t._v("+")])])])])]),e("div",{staticClass:"total"},[t._v("总价："),e("em",[t._v("￥"+t._s(t.book.price*t.book.count))])]),e("div",{staticClass:"operate_btn"},[e("button",{staticClass:"buy_btn",on:{click:t.orderIt}},[t._v("立即购买")]),e("button",{staticClass:"add_cart",on:{click:t.addtoCart}},[t._v("加入购物车")])])])])])},n=[],i=(e("b0c0"),e("a4d3"),e("e01a"),e("1bab")),a={name:"",data:function(){return{book:{id:"1",name:"魔理沙的魔法书",description:"daze",price:39.99,sold_count:999,image:"",stock_count:99,author:"雾雨魔理沙",publisher:"雾雨魔法店",category:"魔导书",count:1}}},created:function(){this.book.id=this.$route.query.book_id,this.getTheBook()},methods:{getTheBook:function(){var t=this,o=new FormData;o.append("book_id",this.book.id),Object(i["a"])({method:"get",url:"/api/base/book_info/",data:o}).then((function(o){if(o.error_num)t.$message({type:"error",message:"获取图书信息失败"});else{var e=o.fields;t.book.name=e.name,t.book.description=e.description,t.book.price=e.price,t.book.sold_count=e.sold_count,t.book.image=e.image,t.book.stock_count=e.stock_count,t.book.author=e.author,t.book.publisher=e.publisher,t.book.category=e.category,t.$set(t.book,"count",1)}})).catch((function(o){console.log(o),t.$message({type:"error",message:"获取图书信息失败"})}))},orderIt:function(){var t=[],o={book_id:this.book.id,book_name:this.book.name,book_price:this.book.price,book_img:this.book.image,book_author:this.book.author,book_count:this.book.count};t.push(o),this.$router.push({path:"/order",query:{orderlist:JSON.stringify(t)}})},addtoCart:function(){var t=this,o=new FormData;o.append("book_id",this.book.id),o.append("book_count",this.book.count),console.log(o),Object(i["a"])({method:"post",url:"/api/trade/add_to_shoppingcart/",data:o}).then((function(o){console.log(o),o.error_num?t.$message({type:"error",message:"加购失败"}):t.$message({type:"success",message:"加购成功"})})).catch((function(o){console.log(o),t.$message({type:"error",message:o.message})}))},countAdd:function(){this.book.count++},countSub:function(){this.book.count>1&&this.book.count--},searchAuthor:function(){this.$router.push({name:"Search",query:{book_author:this.book.author}})}}},s=a,c=(e("89a4"),e("2877")),u=Object(c["a"])(s,r,n,!1,null,null,null);o["default"]=u.exports},e01a:function(t,o,e){"use strict";var r=e("23e7"),n=e("83ab"),i=e("da84"),a=e("5135"),s=e("861d"),c=e("9bf2").f,u=e("e893"),f=i.Symbol;if(n&&"function"==typeof f&&(!("description"in f.prototype)||void 0!==f().description)){var l={},b=function(){var t=arguments.length<1||void 0===arguments[0]?void 0:String(arguments[0]),o=this instanceof b?new f(t):void 0===t?f():f(t);return""===t&&(l[o]=!0),o};u(b,f);var d=b.prototype=f.prototype;d.constructor=b;var p=d.toString,h="Symbol(test)"==String(f("test")),v=/^Symbol\((.*)\)[^)]+$/;c(d,"description",{configurable:!0,get:function(){var t=s(this)?this.valueOf():this,o=p.call(t);if(a(l,t))return"";var e=h?o.slice(7,-1):o.replace(v,"$1");return""===e?void 0:e}}),r({global:!0,forced:!0},{Symbol:b})}},e538:function(t,o,e){var r=e("b622");o.f=r},e8b5:function(t,o,e){var r=e("c6b6");t.exports=Array.isArray||function(t){return"Array"==r(t)}}}]);
//# sourceMappingURL=chunk-5bb7816d.ca6778b1.js.map
<template>
  <div id="home">
    <div class="list-main">
	<div class="container">
		<ul class="select">
			<li class="select-list">
				<dl id="select1">
					<dt>分类：</dt>
					<dd class="select-all selected"><a href="#">全部</a></dd>
					<dd @click="change(index)" :class='{active: selected}'><a href="#" >计算机</a></dd>
					<dd><a href="#">轻小说</a></dd>
					<dd><a href="#">古典</a></dd>
				</dl>
			</li>
		</ul>
		<div class="tabs book clearfix">
			<dl v-for="item in Allbooks" :key="item.pk" class="book-display">
				<dt><img :src="item.fields.image" @click="toDetails(item)"/></dt>
				<dd>
					<p><a @click="toDetails(item)">{{item.fields.name | ellipsis}}</a></p>
					<p>作者：{{item.fields.author | ellipsis}}</p>
					<p>￥{{parseFloat(item.fields.price)}}</p>
				</dd>
			</dl>
		</div>
	</div>
  </div>
  </div>
</template>

<script>
import {request} from "@/network/request.js";

export default {
  data() {
    return {
      keyword: '',
      select_key: '',

      Allbooks: [
        // {
        //   pk: '1',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙fvdaweyvdjwbra vbrwevryvebwfbewfbweb vfbewb',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙bhbaschjgvwdjkuvwqykr',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书hjafueyvgWYEGFEWIF',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
        // {
        //   pk: '2',
        //   fields:{
        //     name: '魔理沙的魔法书',
        //     description: 'daze',
        //     price: 39.99,
        //     sold_count: 999,
        //     image: '',
        //     stock_count: 99,
        //     author: '雾雨魔理沙',
        //     publisher: '雾雨魔法店',
        //     category: '魔导书',
        //   }
        // },
      ]
    }
  },
  created() {
    this.getBooks();
  },
  filters: {
    ellipsis (value) {
      if (!value) return ''
      if (value.length > 10) {
        return value.slice(0,10) + '...'
      }
      return value
    }
  },
  methods: {
    getBooks() {
      request({
      method: 'get',
      url:'api/base/show_books/',
      }).then(res =>{
      console.log(res);
      if(!res.error_num) {
        this.Allbooks = res.data;
      } else {
        this.$message({
          type: 'error',
          message: '获取图书信息失败'+res.message
        })
      }
      }).catch(err => {
      this.$message({
        type: 'error',
        message: '获取图书信息失败'+res.message
      })
      })
    },
    toDetails(item) {
      //发送id，在详情页加载信息
      this.$router.push({path: '/details', query: {book_id: item.pk}});
    },
  },
  components: {

  }
}
</script>

<style>
  	a{ text-decoration:none;  color: #666;}
	a:hover{ text-decoration:none; color:#46b448;}
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
    content: "";
    clear: both;
    display: block;
}
	.container {
    width: 1200px;
    margin: 0 auto;
}
.list-main .container{
	border:#ddd 1px solid;
	border-radius:4px;
	margin-top: 20px;
}

.select{padding:5px 10px;width:1180px; font-size: 14px;}
.select li{list-style:none;padding:10px 0 5px 100px;}
.select .select-list{border-bottom:#eee 1px dashed}
.select dl{zoom:1;position:relative;line-height:24px;}
.select dl:after{content:" ";display:block;clear:both;height:0;overflow:hidden}
.select dt{width:100px;margin-bottom:5px;position:absolute;top:0;left:-100px;text-align:right;color:#666;height:24px;line-height:24px}
.select dd{float:left;display:inline;margin:0 0 5px 5px;}
.select dd.hide{display:none;}
.select a{display:inline-block;white-space:nowrap;height:24px;padding:0 10px;text-decoration:none;color:#039;border-radius:2px;}
.select a:hover{color:#f60;background-color:#f3edc2}
.select .selected a{color:#fff;background-color:#f60}
.tabs{
	padding: 5px 27px;
}
.book dl{
	float: left;
	margin: 10px 10px 10px 10px;
	width: 143px;
  height:280px;
}
.book dl dt{
	border: 1px solid #dee8ef;
	padding: 7px 10px 5px 10px;

}
.book dl dt img{
	width: 123px;
	height: 177px;
	font-size: 0;
}
.book dl dd{
	text-align: center;
	margin-top: 5px;
}
.book dl dd p:first-child a{
	font-size: 14px;
	color: #333;
}
.book dl dd p:nth-child(2){
	font-size: 14px;
	color: #999;
}
.book dl dd p:nth-child(3){
	font-size: 16px;
	color: red;
}
.book dl dd p:nth-child(3) s{
	color: #999;
	font-size: 12px;
}
</style>
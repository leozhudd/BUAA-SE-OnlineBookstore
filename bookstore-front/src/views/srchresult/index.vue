<template>
  <div id="SearchRes">
    <div class="list-main">
	<div class="container">
		<ul class="select">
			<li class="select-list">
				<dl id="select1">
					<dt>分类：</dt>
					<dd class="select-all selected"><a href="#">全部</a></dd>
					<dd><a href="#">计算机</a></dd>
					<dd><a href="#">轻小说</a></dd>
					<dd><a href="#">古典</a></dd>
				</dl>
			</li>
		</ul>
		<div class="tabs book clearfix">
			<dl v-for="item in Allbooks" :key="item.pk">
				<dt><a href=""><img src="item.fields.image" /></a></dt>
				<dd>
					<p><a href="">{{item.fields.name}}</a></p>
					<p>作者：{{item.fields.author}}</p>
					<p>￥{{parseFloat(item.fields.price)}}</p>
				</dd>
			</dl>
		</div>
	</div>
  </div>
  </div>
</template>

<script>
export default {
    name: 'Srchresult',
    data() {
      return {
          resultlist: [
              {
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
              },
              {
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
              }
          ],
      }
    },
    //二次搜索不行
    created() {
      this.resultlist = JSON.parse(this.$route.query.resultlist);
    },
    activated() {
      this.resultlist = JSON.parse(this.$route.query.resultlist);
    },
    methods: {
        toDetails(item) {
          this.$router.push({path: '/details', query: {book_id: item.pk}});
        }
    }
}
</script>

<style>

</style>
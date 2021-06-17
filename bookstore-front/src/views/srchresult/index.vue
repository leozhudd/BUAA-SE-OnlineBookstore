<template>
  <div id="SearchRes">
    <table>
      <tbody>
        <tr v-for="item in resultlist" :key="item.id">
          <td class="td-product">
            <img :src="item.fields.image" width="120" height="150" @click="toDetails(item)">
            <div class="product-info">
              <h6>{{item.fields.name}}</h6>
              <p>作者：{{item.fields.author}}</p >
              <p>出版社：{{item.fields.publisher}}</p >
              <p>单价：￥{{parseFloat(item.fields.price)}}</p >
              <p>分类：{{item.fields.category}}</p >
            </div>
            <div class="clearfix"></div>
          </td>
        </tr>
      </tbody>
    </table>
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
    created() {
      this.resultlist = JSON.parse(this.$route.query.resultlist);
    },
    methods: {
        toDetails(item) {
          this.$router.push({path: '/details', query: {book_id: item.id}});
        }
    }
}
</script>

<style>

</style>
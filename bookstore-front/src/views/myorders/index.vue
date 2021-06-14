<template>
  <div>
    <sub-order></sub-order>
  </div>
</template>

<script>
export default {
    name: 'Myorders',
    data() {
        return {
          orders: []
        }
    },
    methods: {
        getOrders() {
          request({
            method: 'get',
            url: '/api/trade/all_orders_with_details/'
          }).then(res => {
            console.log(res);
            if (!res.error_num) {
              this.orders = res.data;
            } else {
              this.$message({
                type: 'error',
                message: '获取订单信息失败'+res.message
              })
            }
          }).catch(err => {
            console.log(err);
            this.$message({
              type: 'error',
              message: '获取订单信息失败'
            })
          })
            
        }
    },
    components: {
        subOrder,
    }
}
</script>

<style>
</style>
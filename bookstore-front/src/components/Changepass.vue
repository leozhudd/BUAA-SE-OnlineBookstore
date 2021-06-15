<template>
  <div>
    <div>输入旧密码:<input v-model="oldpass"></div>
    <div>输入新密码:<input v-model="newpass1"></div>
    <div>确认新密码:<input v-model="newpass2"></div>
    <button @click="submitChange">确认修改</button>
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

</style>
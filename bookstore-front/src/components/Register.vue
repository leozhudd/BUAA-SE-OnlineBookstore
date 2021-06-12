<template>
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <el-form-item label="用户名" prop="name"><el-input v-model="ruleForm.name" clearable></el-input></el-form-item>
    <el-form-item label="邮箱" prop="email"><el-input v-model="ruleForm.email" clearable></el-input></el-form-item>
    <el-form-item label="密码" prop="pass"><el-input type="password" v-model="ruleForm.pass" auto-complete="off" clearable></el-input></el-form-item>
    <el-form-item label="确认密码" prop="checkPass"><el-input type="password" v-model="ruleForm.checkPass" auto-complete="off" clearable></el-input></el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import {request} from '@/network/request.js'
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass');
        }
        callback();
      }
    };

    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };

    // var validateEmail = (rule, value, callback) => {
    //   if (value === '') {
    //     callback(new Error('请输入邮箱'));
    //   } else if (value.indexOf('@') === -1) {
    //     callback(new Error('错误邮箱格式'));
    //   } else if (value.indexOf('.com') === -1) {
    //     callback(new Error('错误邮箱格式'));
    //   } else {
    //     callback();
    //   }
    // }

    return {
      activeName: 'second',
      ruleForm: {
        name: '',
        email: '',
        pass: '',
        checkPass: ''
      },
      rules: {
        name: [{ required: true, message: '请输入您的名称', trigger: 'blur' }],
        email: [{ required: true,message:'请输入邮箱地址' ,trigger: 'blur'},
        {type:'email', message:'请输入正确的邮箱地址', trigger:['blur','change']}],
        pass: [{ required: true, validator: validatePass, trigger: 'blur' }],
        checkPass: [{ required: true, validator: validatePass2, trigger: 'blur' }]
      }
    };
  },

  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          let sendData = new FormData()
          sendData.append('username',this.ruleForm.name)
          sendData.append('password1', this.ruleForm.pass)
          sendData.append('password2', this.ruleForm.checkPass)
          sendData.append('email', this.ruleForm.email)
          console.log(sendData);

          request({
            method:'post',
            url:'/api/base/register/',
            data: sendData
          }).then(
            response=>{
              console.log(response);
              if(!response.error_num)
              {
                this.$message({
                  type: 'success',
                  message: '注册成功'
                });

                this.$router.push('/');
              }
              else
              {
                this.$message({
                  type:'error',
                  message: response.message
                });
              }
            }
          ).catch(error => {
            this.$message({
              type:'error',
              message: error.message
            });
            return false;
          })
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    toLogin() {
          let sendData = new FormData()
          sendData.append('username',this.ruleForm.name)
          sendData.append('password', this.ruleForm.pass)
          console.log(sendData);
          
          request({
            method: 'post',
            url: '/api/base/login/',
            data: sendData
          })
          .then(response=>{
            console.log(response);
            if(!response.error_num)
            {
              this.$message({
                type: 'success',
                message: '登录成功'
              });
              localStorage.setItem("username",this.ruleForm.name);
              this.$store.commit('login');
              console.log(this.$store.state.isLogin);
              
              this.$router.push('/');
              this.$router.go(0);
            }
            else
            {
              this.$message({
              type: 'error',
              message: response.message,
              });
              return false;
            }
            }).catch(error=>{
            console.log(error);
            this.$message({
              type: 'error',
              message: error.message
            });
          });
    }
  }
};
</script>

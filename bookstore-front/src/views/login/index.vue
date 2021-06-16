<template>
  <div class="login-container">
  <div class="login">
    <el-tabs v-model="activeName" @tab-click="handleClick" class="login-tabs">
      <el-tab-pane label="登录" name="first">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="用户名" prop="name"><el-input v-model="ruleForm.name" clearable></el-input></el-form-item>

          <el-form-item label="密码" prop="pass"><el-input type="password" v-model="ruleForm.pass" auto-complete="off" clearable></el-input></el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
          </el-form-item>
        </el-form>


        <el-button type="text" @click="centerDialogVisibleSecond = true">找回密码</el-button>

        <el-dialog
          title="密码找回"
          :visible.sync="centerDialogVisibleSecond"
          width="30%"
          :before-close="handleClose">
          <span>
                    <el-form label-width="120px" ref="forgetpwdform" :model="forgetpwdform" :rules="rules">
                        <el-row :gutter="20">
                            <el-col :span="17">
                                <el-form-item prop="email" label="邮箱：">
                                    <el-input v-model="forgetpwdform.email" maxlength="20" clearable></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="7">
                                <el-button @click="sendEmail" :disabled="disabled">{{sendcode}}</el-button>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col>
                                <el-form-item prop="code" label="验证码：">
                                    <el-input v-model="forgetpwdform.code"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-form-item prop="newpassword" label="新密码">
                            <el-input type="password" v-model="forgetpwdform.newpassword" clearable></el-input>
                        </el-form-item>
                        <el-form-item prop="repeatpassword" label="确认密码">
                            <el-input type="password" v-model="forgetpwdform.repeatpassword" clearable></el-input>
                        </el-form-item>

                    </el-form>


          </span>
          <span slot="footer" class="dialog-footer">
            <el-button type="default" @click="handleClose">取 消</el-button>
            <el-button type="primary" @click="handleSubmit">确 定</el-button>
          </span>
        </el-dialog>



      </el-tab-pane>

      <el-tab-pane label="注册" name="second">
        <register></register>
      </el-tab-pane>
    </el-tabs>

  </div>
  </div>
</template>

<script>
import register from '@/components/Register';
import qs from "qs";
import {request} from "@/network/request.js";

export default {
  name: "forgetpwd",
  props: ["centerDialogVisibleSecond"],
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

    return {
      activeName: 'first',
      ruleForm: {
        name: '',
        pass: '',
        checkPass: ''
      },
      getCode: "",
      sendcode: "发送验证码",
      disabled: false,
      centerDialogVisibleSecond: false,
      forgetpwdform: {
          email: "",
          code: "",
          newpassword: "",
          repeatpassword: ""
      },
      rules: {
          name: [{ required: true, message: '请输入您的名称', trigger: 'blur' }],
          pass: [{ required: true, validator: validatePass, trigger: 'blur' }],

          email: [
              {required: true, message: "邮箱不能为空", trigger: "blur"}
          ],
          code: [
              {
                  required: true, message: "验证码不能为空", trigger: "blur"
              },
          ],
          newpassword: [
              {
                  required: true, message: "新密码不能为空", trigger: "blur"
              },
          ],
          repeatpassword: [
              {
                  required: true, message: "重置密码不能为空", trigger: "blur"
              }
          ]
      }


    };
  },

  methods: {
    //选项卡切换
    handleClick(tab, event) {},
    //提交表单
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
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
              //this.$router.push('/');
              //this.$router.go(0);
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
      } else{
            this.$message({
              type: 'error',
              message: '输入格式不正确'
            });
        return false;
      }
      });
    },

    //判断邮箱格式是否符合要求
    judgeEmail() {
        const reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        //var url="/nptOfficialWebsite/apply/sendSms?mobile="+this.ruleForm.email;
        if (this.forgetpwdform.email == '') {
            this.$message("请输入邮箱")
            return false;
        } else if (!reg.test(this.forgetpwdform.email)) {
            this.$message("邮箱格式不正确")
            return false;
        } else {
            return true;
        }
    },


    //发送邮箱验证码
    sendEmail() {
        let _this = this;
        if (_this.judgeEmail()) {
            var num = 60;
            var timer = setInterval(function () {
                num--;
                _this.disabled = true;
                _this.sendcode = num + '秒后重新获取';
                if (num === 0) {
                    _this.sendcode = '获取验证码';
                    _this.disabled = false;
                    clearInterval(timer)
                }
            }, 1000)
            _this.$http.post("接口", qs.stringify(
                {emailNumber: _this.forgetpwdform.email}
            )).then((res) => {
                _this.getCode = res;
            })
        }

    },


    //关闭页面
    handleClose() {
        this.centerDialogVisibleSecond = false;
        this.$emit("tyonke", this.centerDialogVisibleSecond);
    },

    //表单提交
    handleSubmit() {
        let _this = this;
        _this.$refs['forgetpwdform'].validate(valid => {
            if (valid) {
                if (_this.forgetpwdform.code != _this.getCode) {
                    this.$message({
                        type: "error",
                        message: "修改失败",
                        duration: 1000
                    })
                    return false;
                }
                return this.$message({
                    type: "success",
                    message: "修改成功",
                    duration: 1000
                })
            } else {
                return
            }
        })
    },

  },

  components: {
    register
  },

  watch: {
      centerDialogVisibleSecond(newValue, oldValue) {
          this.centerDialogVisibleSecond = newValue;
      }
  },

};
</script>

<style>
.login-container {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: rgb(216, 132, 5);
}

.login {
  width: 500px;
  height: 700px;
  margin: 0 auto;
}

.login-tabs {
  width: 350px;
  margin: 10px auto; /* 上下间距160px，左右自动居中*/
  background-color: rgb(255, 255, 255, 0.8); /* 透明背景色 */
  padding: 30px;
  border-radius: 2px; /* 圆角 */
}
</style>

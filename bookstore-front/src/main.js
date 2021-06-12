import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

Vue.config.productionTip = false
Vue.prototype.$axios = axios
//允许浏览器发送cookies
axios.defaults.withCredentials = true;
//axios.defaults.headers.post['Content-Type'] = 'application/json';

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

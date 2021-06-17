import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
    login() {
      localStorage.setItem("isLogin",true);
    },
    logout() {
      localStorage.setItem("isLogin",false);
    }
  },
  actions: {
  },
  modules: {
  }
})

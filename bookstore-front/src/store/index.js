import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
  },
  mutations: {
    login(name) {
      state.isLogin = true;
    },
    logout() {
      state.isLogin = false;
    }
  },
  actions: {
  },
  modules: {
  }
})

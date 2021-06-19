import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: window.localStorage.getItem('user'),
    isLogin: window.localStorage.getItem('isLogin'),
  },
  mutations: {
    login:(state, data)=> {
      state.user = data;
      state.isLogin = true;
      localStorage.setItem('isLogin',true);
      localStorage.setItem('user',data);
    },
    logout:(state)=> {
      state.isLogin = false;
      localStorage.setItem('user', null);
      localStorage.setItem('isLogin',false);
    }
  },
  actions: {

  },
  modules: {

  }
})

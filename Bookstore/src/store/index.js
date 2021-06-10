import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    onlineuser: '',
  },
  mutations: {
    login(name) {
      state.onlineuser = name;
    },
    logout() {
      state.onlineuser = '';
    }
  },
  actions: {
  },
  modules: {
  }
})

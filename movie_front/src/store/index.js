import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'
Vue.use(Vuex)

export default new Vuex.Store({
  // 상태 (data)
  state: {
    token : null,
  },
  // computed
  getters:{
    isLoggedIn(state){
      return state.token ? true : false
    },
    options(state){
      return {
        headers:{
          Authorization : 'JWT ' + state.token 
        }
      }
    },
    userId(state){
      return state.token ? jwtDecode(state.token).user_id : null
    },
  },
  // 상태를 변경하는 함수
  mutations: {
    setToken(state, token){
      state.token = token
    }
  },
  // methods
  actions: {
    login(context, token){
      context.commit('setToken', token)
    },
    logout(context){
      context.commit('setToken', null)
    }
  },


  modules: {
  }
})
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/login')
  },
  {
    path: '/shoppingcart',
    name: 'Shoppingcart',
    component: () => import('../views/shoppingcart')
  },
  {
    path: '/details',
    name: 'Details',
    component: () => import('../views/details')
  },
  {
    path: '/order',
    name: 'Order',
    component: () => import('../views/order')
  },
  {
    path: '/myorders',
    name: 'Myorders',
    component: () => import('../views/myorders')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

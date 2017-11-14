import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Teams from '@/components/Teams'
import Players from '@/components/Players'
import FunFacts from '@/components/FunFacts'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/teams',
      name: 'Teams',
      component: Teams
    },
    {
      path: '/players',
      name: 'Players',
      component: Players
    },
    {
      path: '/facts',
      name: 'FunFacts',
      component: FunFacts
    }
  ]
})

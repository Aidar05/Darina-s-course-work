import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GalleryView from "../views/GalleryView.vue"
import RegView from '@/views/RegView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/gallery',
    name: 'gallery',
    component: GalleryView
  },
  {
    path: '/reg',
    name: 'reg',
    component: RegView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

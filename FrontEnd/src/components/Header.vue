<template>
  <div class="header">
    <router-link to="/" class="logo">LOGO</router-link>

    <div class="header-menu">
      <router-link v-for="(element, index) in menuElements" :key="index"  
        :to="'/' + element.link" class="menu-element">
        {{ element.text }}
      </router-link>
    </div>

    <div class="reg-container" v-if="!logged_in">
      <router-link to="/">Регистрация</router-link>
      <router-link to="/">Войти</router-link>
    </div>

    <div class="profile" v-else></div>
  </div>
</template>

<script>
export default{
  name: "Header",
  data(){
    return{
      logged_in: false,
      menuElements: [
        {text: "Ван Гок", link: "Van-Gock-container"},
        {text: "история работ", link: "works"},
        {text: "галерея", link: "/gallery"},
        {text: "критики", link: "critics"}
      ]
    }
  }
}
</script>
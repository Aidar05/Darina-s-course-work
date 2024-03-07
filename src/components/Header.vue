<template>
  <div class="header">
    <router-link to="/" class="logo">LOGO</router-link>
    
    <div class="header-menu">
      <router-link v-for="(element, index) in menuElements" :index="key"  
        to="element.link" class="menu-element">
        {{ element.text }}
      </router-link>
    </div>
  </div>
</template>

<script>
export default{
  name: "Header",
  data(){
    return{
      menuElements: [
        {text: "Ван Гок", link: "Van-Gock"},
        {text: "история работ", link: "works"},
        {text: "галерея", link: "/gallery"},
        {text: "критики", link: "critics"}
      ]
    }
  }
}
</script>
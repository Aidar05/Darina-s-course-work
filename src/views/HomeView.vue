<template>
  <Header></Header>
    
  <div class="main-container">
    <article class="quote-container">
      <p id="quote" v-html="quote"></p>

      <span id="quote-author">{{ quoteAuthor }}</span>
    </article>
  </div>
</template>

<script>
import Header from "@/components/Header.vue"

export default {
  name: 'HomeView',
  components: {
    Header
  },
  data(){
    return{
      quote: '„Я вложил свое сердце и <br> душу в свою \
        <span id="highlight-work">работу</span>, \
        и я <br> сошел с ума в процессе.“',
      quoteAuthor: "— Винсент Ван Гок"
    }
  }
}
</script>

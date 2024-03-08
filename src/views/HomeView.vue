<template>
  <Header></Header>
    
  <div class="main-container">
    <article class="quote-container">
      <p id="quote" v-html="quote"></p>

      <span id="quote-author">{{ quoteAuthor }}</span>
    </article>

    <div id="Van-Gock-container">
      <img src="../assets/imgs/VanGock.png" alt="Resource not found" id="Van-Gock-img">

      <div id="about-text-container">
        <h1 id="about-header">{{ aboutHeader }}</h1>

        <p id="about-text">{{ aboutText }}</p>

        <button class="call-to-action">{{ buttonText }}</button>
      </div>
    </div>
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
        и я <br> сошел c ума в процессе.“',
      quoteAuthor: "— Винсент Ван Гок",
      aboutHeader: "Кратко про Винсента Ван Гока", 
      aboutText: "Винсе́нт Ви́ллем Ван Гог — нидерландский художник-постимпрессионист, чьи работы \
        оказали значительное влияние на живопись XX века. За десять с небольшим лет создал более \
        2 100 произведений, включая около 870 картин маслом. При жизни был практически обойдён \
        вниманием критиков.",
      buttonText: "в галерею"
    }
  }
}
</script>

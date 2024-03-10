<template>
  <Header></Header>
    
  <div class="main-container">
    <article class="quote-container">
      <p id="quote" v-html="quote"></p>

      <span id="quote-author">{{ quoteAuthor }}</span>
    </article>
  </div>

  <div class="main-container">
    <div id="Van-Gock-container">
      <img src="../assets/imgs/VanGock.png" alt="Resource not found" id="Van-Gock-img">

      <div id="about-text-container">
        <h1 id="about-header">{{ aboutHeader }}</h1>

        <p id="about-text">{{ aboutText }}</p>

        <button class="call-to-action">{{ buttonText }}</button>
      </div>
    </div>
  </div>

  <div class="main-container">
    <Works v-for="(item, index) in worksContent" :key="index" :workHeader="item.header" :workText="item.text"
     :imgSrc="item.img" :bgColor="item.bgColor" :imgInfo="item.imgInfo" :museum="item.museum">
    </Works>
  </div>
</template>

<script>
import Header from "@/components/Header.vue"
import Works from "@/components/Works.vue"

export default {
  name: 'HomeView',
  components: {
    Header, Works
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
      buttonText: "в галерею",
      worksContent: [
        { header: "Валуны и дуб", bgColor: "orange",
          text: "Картина «Валуны и дуб» была написана летом 1888 года, когда \
            Винсент ван Гог жил в городке Арль, находящемся на юге Франции. Арльский период считается \
            наиболее плодотворным периодом творческой биографии художника. Пейзаж, изображённый на \
            картине, находился в гористой местности Монмажур  расположенной в нескольких  километрах \
            к северу от Арля. К тому же периоду относится серия набросков видов Монмажура, хранящаяся \
            в Музее Винсента ван Гога в Амстердаме.",
          img: require("../assets/imgs/boulders.png"), imgInfo: "Холст, масло. 54,9 x 65,7 см",
          museum: "Музей изящных искусств, Хьюстон"

        }
      ]
    }
  }
}

</script>

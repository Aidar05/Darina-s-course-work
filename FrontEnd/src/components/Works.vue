<template>
  <div class="work-element" :class="(bgColor)">
    <article class="work-text-container">
      <h1 class="work-header">{{ workHeader }}</h1>

      <p class="work-text">{{ workText }}</p>
    </article>
    
    <div class="work-img-container">
      <img :src="imgSrc" alt="Resource not found" class="work-img">

      <div class="credit-container">
        <span class="img-info">{{ imgInfo }}</span>
        <span class="img-info museum">{{ museum }}</span>
        <div class="line first-line"></div>
        <div class="line second-line"></div>
      </div>
      
    </div>
  </div>
</template>

<script>
export default{
  name: "Works",
  props: {
    workHeader: String,
    workText: String,
    imgSrc: String,
    bgColor: String,
    imgInfo: String,
    museum: String  
  }
}
</script>
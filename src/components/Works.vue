<template>
  <div id="works">
    <div class="work-element" :class="(bgColor)">
      <article class="work-text-container">
        <h1 class="work-header">{{ workHeader }}</h1>

        <p class="work-text">{{ workText }}</p>
      </article>
      
      <div class="work-img-container">
        <img :src="imgSrc" alt="Resource not found" class="work-img">
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
    imgSrc: String
  }
}
</script>
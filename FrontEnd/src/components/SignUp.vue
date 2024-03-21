<template>
  <div class="reg-container">
    <form @submit.prevent="submitForm" action="/sign-up" method="post" class="reg-form">
      <input
        v-model="form.username"
        type="text"
        placeholder="username"
        name="username"
        autocomplete="off"
        class="reg-input">
      
      <input
        v-model="form.email"
        type="email"
        placeholder="email"
        name="email"
        autocomplete="off"
        class="reg-input">

      <input
        v-model="form.password"
        type="password"
        placeholder="password"
        name="password"
        autocomplete="off"
        class="reg-input">

      <a href="/sign-in" class="sign-in-link">Уже есть аккаунт?</a>

      <button type="submit" class="ghost-btn reg-btn">Создать</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "SignUp",
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    submitForm() {
      const formData = new URLSearchParams();
      formData.append('username', this.form.username);
      formData.append('email', this.form.email);
      formData.append('password', this.form.password);
      
      axios.post('http://localhost:5000/sign-up', this.form, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
}
</script>
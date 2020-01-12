<template>
  <div class="container">
    <h1>Log In</h1>
    <hr>
    <LoginForm />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import router from "@/router";
import LoginForm from '@/components/LoginForm'
export default {
  name: 'Login',
  components: {
    LoginForm, 
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  created(){
    if (this.isLoggedIn) {
      router.push('/home')
    }
  }
}
</script>

<style>
.container {
  min-height: 100%;
  border: 0;
  padding: 0;
}
</style>
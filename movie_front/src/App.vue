<template>
  <div id="app">
    <link href="https://fonts.googleapis.com/css?family=Jua&display=swap" rel="stylesheet">
    <div id="nav" v-if="isLoggedIn" class="header clearfix navbar-expand-sm navbar-light">
      <div class>
        <router-link to="/home">Movie Information</router-link>
        <a class="float-right" @click.prevent="logout" href="logout/">Logout</a>
        <span class="float-right mx-1">|</span>
        <router-link class="float-right" to="/userprofile">My Profile</router-link>
        <span class="float-right mx-1">|</span>
        <router-link class="float-right" to="/userpage">My Movies</router-link>
      </div>
      <!-- <div v-else class="header clearfix navbar-expand-sm navbar-light">
        <router-link to="/">Movie Infomation</router-link>
        <router-link class="float-right" to="/login" >Login</router-link>
        <span class="float-right mx-1"> | </span>
        <router-link class="float-right" to="/signup" >Signup</router-link>
      </div> -->
  

      <go-top :size="40" :z-index="800" :bottom="30" :right="25" bg-color="#42b983"></go-top>
    </div>
    <div class="body">
      <router-view />
    </div>
  </div>
</template>


<script>
import { mapGetters } from "vuex";
import router from "@/router";
import GoTop from "@inotom/vue-go-top";
export default {
  name: "App",
  data() {
    return {};
  },
  components: {
    GoTop
  },
  methods: {
    logout() {
      this.$session.destroy();
      this.$store.dispatch("logout");
      router.push("/");
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  created() {
    if (this.$session.has("jwt")) {
      const token = this.$session.get("jwt");
      this.$store.dispatch("login", token);
    }
  }
};
</script>

<style>
#app {
  font-family: 'Jua', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  font-size: 25px;
}
#nav a {
  font-weight: bold;
  color: white;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
.header {
  border: 0;
  padding: 0;
  background-color: black;
  min-height: 100%;
  background-position: center;
  background-size: cover;
  opacity: 0.8;
  filter: alpha(opacity=40);
}
.body {
  border: 0;
  padding: 0;
  background-image: url("assets/images/background.png");
  min-height: 100%;
  background-position: center;
  background-size: cover;
  color: white;
}
</style>
<template>
  <div>
    <div
      class="position-fixed text-center"
      vertical
      style="width:100%; margin-top: 10%; font-size:6rem; color:white;">J O K E R S T</div>
    <b-button-group
      size="lg"
      class="position-fixed"
      vertical
      style="width: 20%; margin-top: 30%; margin-left:40%;"
    >
      <b-button v-b-modal.loginModal pill variant="success" class="mb-4 font-weight-bold">Login</b-button>
      <b-modal header-bg-variant="success" body-bg-variant="light" header-text-variant="white" hide-footer id="loginModal" title="Log in">
        <LoginForm />
      </b-modal>
      <b-button v-b-modal.signupModal pill variant="success" class="mb-4 font-weight-bold">Singup</b-button>
      <b-modal header-bg-variant="success" body-bg-variant="light" header-text-variant="white" hide-footer id="signupModal" title="Sign up">
        <SignupForm />
      </b-modal>
    </b-button-group>
    <b-img
      :src="require('../assets/images/mainback.png')"
      fluid-grow
      alt="image"
      style="position:absolute; filter: blur(5px); z-index:-1; border: 0px;"
    ></b-img>
  </div>
</template>

<script>
import LoginForm from "@/components/LoginForm";
import SignupForm from "@/components/SignupForm";

import { mapGetters } from "vuex";
import router from "@/router";
export default {
  name: "Mainpage",
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  components: {
    LoginForm,
    SignupForm
  },
  methods: {},
  created() {
    if (this.isLoggedIn) {
      router.push("/home");
    }
  }
};
</script>

<style>
/* #bg-img {
  border: 0;
  padding: 0;
  background-image: url("../assets/images/mainback.png");
  min-height: 100%;
  background-position: center;
  background-size: cover;
} */
</style>
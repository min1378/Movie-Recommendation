<template>
  <div class="signup-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading..</span>
    </div>

    <div v-else class="signup-form">
      <div v-if="errors.length" class="alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr />
        <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
      </div>

      <div class="form-group">
        <label for="id">ID</label>
        <input
          type="text"
          id="id"
          class="form-control"
          placeholder="ID를 입력해주세요."
          v-model="credentials.username"
        />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          class="form-control"
          placeholder="Password를 입력해주세요."
          v-model="credentials.password"
        />
      </div>
      <div class="form-group">
        <label for="password_check">Password 확인</label>
        <input
          type="password"
          id="password_check"
          class="form-control"
          placeholder="Password를 다시한번 입력해주세요."
          v-model="credentials.password_check"
        />
      </div>

      <div class="form-group">
        <label for="email">E-mail</label>
        <input @keydown.enter="signup"
          type="text"
          id="email"
          class="form-control"
          placeholder="E-mail을 입력해주세요."
          v-model="credentials.email"
        />
      </div>

      <div class="form-group">
        <label for="gender">Gender</label>
        <select id="gender" class="form-control" v-model="credentials.gender">
          <option selected value="0">Man</option>
          <option value="1">Woman</option>
        </select>
      </div>

      <button class="btn btn-success" @click="signup">Sign Up</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";
export default {
  name: "Signup",
  data() {
    return {
      credentials: {
        username: "",
        password: "",
        password_check: "",
        email: "",
        gender: 0
      },
      loading: false,
      errors: []
    };
  },
  methods: {
    signup() {
      if (this.checkForm()) {
        this.loading = true;
        const SERVER_IP = process.env.VUE_APP_SERVER_IP;
        const signUpData = {
          username: this.credentials.username,
          password: this.credentials.password,
          email: this.credentials.email,
          gender: this.credentials.gender,
        }
        
        axios
          .post(SERVER_IP + "/accounts/signup/", signUpData)
          .then( () => {
            axios.post(SERVER_IP + "/api-token-auth/", {username: this.credentials.username, password:this.credentials.password})
              .then(response => {
              this.$session.start();
              this.$session.set("jwt", response.data.token);
              this.$store.dispatch("login", response.data.token);
              this.loading = false
              router.push("/home")
              })
            .catch(error => {
              console.log(error)
              this.loading = false
            })
          })
          .catch(error => {
            console.log(error)
            this.loading = false
          })
      }
    },
    checkForm() {
      this.errors = [];
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.");
      }
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.");
      }
      if (this.credentials.password !== this.credentials.password_check) {
        this.errors.push("비밀번호가 일치하지 않습니다.");
      }
      if (this.credentials.email.indexOf('@')===-1){
        this.errors.push("E-mail 양식에 맞지 않습니다.");
      }
      if (this.errors.length === 0) {
        return true;
      }
    }
  },
  mounted(){
    
  }
};
</script>

<style>
</style>
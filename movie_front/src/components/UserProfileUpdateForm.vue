<template>
  <div class="pb-5">
    <h1>User Profile Update</h1>
    <hr />
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading..</span>
    </div>

    <div v-else class="userupdate-form">
      <div v-if="errors.length" class="alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr />
        <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
      </div>

      <h4 class="mb-4">ID : {{ credential.username }}</h4>
      <div class="form-group" v-if="!checkBool">
        <label for="password">기존 Password</label>
        <input @keydown.enter="checkpassword"
          type="password"
          id="password"
          class="form-control"
          placeholder="기존 Password를 입력해주세요."
          v-model="password"
        />
        <button class="btn btn-primary mt-1" @click="checkpassword">confirm</button>
      </div>
      <div v-else>
        <div>기존 Password</div>
        <h5 class ="mt-2">확인되었습니다.</h5>
      </div>
      <hr />

      <div class="form-group">
        <label for="change_password">Password</label>
        <input
          type="password"
          id="change_password"
          class="form-control"
          placeholder="변경할 Password를 입력해주세요."
          v-model="credentials.change_password"
        />
      </div>
      <div class="form-group">
        <label for="change_password_check">Password 확인</label>
        <input 
          type="password"
          id="change_password_check"
          class="form-control"
          placeholder="Password를 다시한번 입력해주세요."
          v-model="credentials.change_password_check"
        />
      </div>

      <div class="form-group">
        <label for="email">E-mail</label>
        <input @keydown.enter="updateProfile" type="text" id="email" class="form-control" v-model="credentials.email" />
      </div>

      <div class="form-group">
        <label for="gender">Gender</label>
        <select id="gender" class="form-control" v-model="credentials.gender">
          <option selected value="0">Man</option>
          <option value="1">Woman</option>
        </select>
      </div>

      <button class="btn btn-success" @click="updateProfile">Update</button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex"; 
import axios from "axios";
import router from "@/router";
export default {
  name: "UserProfileUpdateForm",
  props: {
    credential: {
      type: Object,
      require: true
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  data() {
    return {
      password: "",
      credentials: {
        change_password: "",
        change_password_check: "",
        email: "asdas ",
        gender: 0
      },
      checkBool:false,
      loading: false,
      errors: []
    };
  },
  methods: {
    checkpassword() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .post(
          `${SERVER_IP}/accounts/check_password/${this.userId}/`,
          { password: this.password },
          this.options
        )
        .then(response => {
          if (response.data === true) {
            console.log(response.data)
            this.checkBool = true
          } else {
            this.errors.push("비밀번호가 틀립니다.");
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    updateProfile(){
      if(this.checkForm() && this.checkBool){
        const SERVER_IP = process.env.VUE_APP_SERVER_IP;
        axios
          .put(
            `${SERVER_IP}/accounts/change/${this.userId}/`,
            { password: this.credentials.change_password, email: this.credentials.email, gender: this.credentials.gender },
            this.options
          )
          .then(() => {
            this.$session.destroy();
            this.$store.dispatch("logout");
            alert('변경 완료되었습니다. 다시 로그인해주세요.')
            router.push("/login");
          })
          .catch(error => {
            console.log(error);
          });
      }
    },

    checkForm() {
      this.errors = [];
      if (this.credentials.change_password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.");
      }
      if (this.credentials.change_password !== this.credentials.change_password_check) {
        this.errors.push("비밀번호가 일치하지 않습니다.");
      }
      if (this.credentials.change_password === this.password) {
        this.errors.push("기존 비밀번호와 동일합니다.");
      }
      if (this.credentials.email.indexOf("@") === -1) {
        this.errors.push("E-mail 양식에 맞지 않습니다.");
      }
      if (this.errors.length === 0) {
        return true;
      }
    }
  },

  mounted() {
    if (this.isLoggedIn) {
      this.credentials.email = this.credential.email;
      this.credentials.gender = this.credential.gender;
    }
  },
};
</script>

<style>
</style>
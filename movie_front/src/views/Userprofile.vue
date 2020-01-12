<template>
  <div class="container py-5" >
    <div v-if="!updateBool">
      <UserProfileForm :credential="credential"  />
      <div>
        <button class="btn btn-primary" @click="goBack">뒤로가기</button>
        <button class="btn btn-success ml-3" @click="update">Update</button>
        <button class="btn btn-danger ml-3" @click="withdraw">Withdraw</button>
      </div>
      <div id="downpage">
        <div v-if="withdrawBool" >
        <hr />
        <div v-if="errors.length" class="alert alert-danger">
          <h4>다음의 오류를 해결해주세요.</h4>
          <hr />
          <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            class="form-control"
            placeholder="Password를 입력해주세요."
            v-model="password"
          />
        </div>
        <button class="btn btn-danger mt-3" @click="withdrawConfirm">Confirm</button>
      </div>

      </div>
      
    </div>
    <div v-else>
      <UserProfileUpdateForm :credential="credential" />
    </div>
  </div>
</template>

<script>
import UserProfileForm from "@/components/UserProfileForm";
import UserProfileUpdateForm from "@/components/UserProfileUpdateForm";
import { mapGetters } from "vuex";
import axios from "axios";
import router from "@/router";

export default {
  name: "Userprofile",
  components: {
    UserProfileForm,
    UserProfileUpdateForm
  },

  data() {
    return {
      updateBool: false,
      withdrawBool: false,
      password: "",
      errors: [],
      credential: {}
    };
  },

  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },

  methods: {
    withdrawConfirm() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      this.errors = [];
      axios
        .post(
          `${SERVER_IP}/accounts/check_password/${this.userId}/`,
          { password: this.password },
          this.options
        )
        .then(response => {
          if (response.data === true) {
            axios
              .delete(
                `${SERVER_IP}/accounts/withdraw/${this.userId}/`,
                this.options
              )
              .then(() => {
                this.$session.destroy();
                this.$store.dispatch("logout");
                router.push("/");
              })
              .catch(error => {
                console.log(error);
              });
          } else {
            this.errors.push("비밀번호가 틀립니다.");
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    update() {
      this.updateBool = true;
    },
    withdraw() {
      this.withdrawBool = this.withdrawBool ? false : true;
    },
    getUserProfile() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/accounts/userprofile/${this.userId}/`, this.options)
        .then(response => {
          console.log(response.data);
          this.credential = {
            username: response.data.username,
            email: response.data.email,
            gender: response.data.gender
          };
        })
        .catch(error => {
          console.log(error);
        });
    },
    goBack() {
      router.go(-1);
    }
  },
  created() {
    if (!this.isLoggedIn) {
      router.push("/login");
    }
    this.getUserProfile();
  }
};
</script>
 

<style>
 #downpage {
    margin-bottom: 35%;
  }
</style>
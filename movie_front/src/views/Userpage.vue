<template>
  <div class="pt-2">
    <div>
      <b-nav tabs align="center" class="font-weight-bold" id="nav-bar">
        <b-nav-item @click="goBack">Back</b-nav-item>
        <b-nav-item  @click="userTabSelect1">My Movies</b-nav-item>
        <b-nav-item @click="userTabSelect2"  variant="primary">My Comment</b-nav-item>
      </b-nav>
    </div>
    <div>
      <UserLikedMovies v-if="userBool" :userLikedMoviesList="userLikedMoviesList" />
      <UserRatings v-else :userRatingsList="userRatingsList" />
    </div>
  </div>
</template>

<script>
import UserLikedMovies from "@/components/UserLikedMovies";
import UserRatings from "@/components/UserRatings";
import axios from "axios";
import { mapGetters } from "vuex";
import router from "@/router"

// import router from "@/router";
export default {
  name: "Userpage",
  components: {
    UserLikedMovies,
    UserRatings
  },
  computed: {
    // ...A ; A 가 가진 아이템 다 뿌려 / js 문법
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  data() {
    return {
      userPage: {},
      userLikedMoviesList: [],
      userRatingsList: [],
      userBool : true
    };
  },
  methods: {
    getLikedMovies() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/accounts/userprofile/${this.userId}/`, this.options)
        .then(response => {
          this.userPage = response.data;
          for (const likedMovieId of this.userPage.liked_movies) {
            axios
              .get(`${SERVER_IP}/api/v1/movies/${likedMovieId}/`, this.options)
              .then(response => {
                this.userLikedMoviesList.push(response.data);
              })
              .catch(error => {
                console.log(error);
              });
          }
          for (const ratingID of this.userPage.ratings) {
            axios
              .get(`${SERVER_IP}/api/v1/ratings/${ratingID}/`, this.options)
              .then(response => {
                this.userRatingsList.push(response.data);
              })
              .catch(error => {
                console.log(error);
              });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    userTabSelect1(){
      this.userBool = true
    },
    userTabSelect2(){
      this.userBool = false
    },
    goBack() {
      router.go(-1);
    },
  },
  created() {
    if (!this.isLoggedIn) {
      router.push('/login')
    }
    this.getLikedMovies();
  }
};
</script>

<style>
 #nav-bar :defined{
   color: white;
   border: none;
 }
 #nav-bar :hover{
   color: #42b983;
 }
</style>
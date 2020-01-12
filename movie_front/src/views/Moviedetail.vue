<template>
  <div class="py-5"> 
    <h1 class="d-flex justify-content-center ">Movie Detail</h1>
    <hr />
    <MovieDetailPage :movie="movie" :director_list="director_list" :actor_list="actor_list" :likeBool="likeBool" @likeUnlike="likeUnlike"/>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import router from "@/router";

import axios from "axios";
import MovieDetailPage from "@/components/MovieDetailPage";

export default {
  name: "Moviedetail",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  components: {
    MovieDetailPage
  },
  data() {
    return {
      movie: {},
      director_list: [],
      actor_list: [],
      likeBool: false
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  methods: {
    getMovieDetail() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/movies/${this.id}/`, this.options)
        .then(response => {
          this.movie = response.data;
          for (const director of this.movie.directors) {
            this.director_list.push(director.name);
          }
          for (const actor of this.movie.actors) {
            this.actor_list.push(actor.name);
          }
          for (let user of this.movie.liked_users) {
            if (user.id == this.userId) {
              this.likeBool = true
            }
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    likeUnlike(bool){
      this.likeBool = bool
    }
  },
  created() {
    if (!this.isLoggedIn) {
      router.push('/login')
    }
    this.getMovieDetail();
  }
};
</script>

<style>
</style>
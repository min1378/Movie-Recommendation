<template>
  <b-card class="card border col-3" title="" :img-src="movie.poster_url" img-alt="poster" >
    <b-card-text>
      <span class="badge badge-success mr-1" v-text="movie.naver_score" ></span>
      <span class="badge badge-danger">♥ {{ movie.liked_users.length }}</span>
      <br />
      <h4 class="card-title mt-1 mb-0" v-text="movie.title" @click="goDetail" style="cursor:pointer; color:black;"></h4>
      <small class="text-muted mb-0" @click="goDetail" style="cursor:pointer;">({{ movie.grade }})</small>
      <small class="text-muted mt-0 d-flex" @click="goDetail" style="cursor:pointer;">개봉일 : {{ movie.opendt }}</small>
    </b-card-text>
  </b-card>
</template> 

<script>
// import axios from "axios";
import router from "@/router";
import { mapGetters } from "vuex";
export default {
  name: "MovieListItem",
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  methods: {
    goDetail() {
      router.push(`/moviedetail/${this.movie.id}`);
    },
  }
};
</script>

<style>
  div.card.border.col-3 {
    padding:0;
    border: none;
  }
  div.card-body{
  }
</style>
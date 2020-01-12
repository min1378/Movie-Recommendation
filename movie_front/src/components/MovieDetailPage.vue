<template>
  <div class="mx-4">
    <div>
      <h2 class="d-flex justify-content-center">{{ movie.title }}</h2>
      <div class="d-flex justify-content-between mx-5" style="height:2rem;">
        <b-button size="sm" class="sm align-self-end" @click="goBack">뒤로가기</b-button>
        <!-- <b-button class="sm align-self-end p-0 b-0" v-if="likeBool" @click="movie_like"> -->
        <h5
          class="text-muted d-inline"
        >{{ movie.title_en }}, {{ String(movie.opendt).substr(0, 4) }}</h5>
        <div>
          <b-button variant="white" class="align-self-end" @click="movie_like">
          <img
            v-if="likeBool" 
            class="sm btn align-self-end p-0"
            style="cursor:pointer;"
            src="@/assets/images/like.png"
            alt="like"
          />
          <img
            v-else
            class="btn sm align-self-end p-0"
            style="cursor:pointer;"
            src="@/assets/images/unlike.png"
            alt="unlike"
          />
        </b-button>
        </div>
      </div>
    </div>
    <hr />
    <b-row class="justify-content-center mx-3">
      <b-col>
        <b-embed type="iframe" aspect="16by9" :src="movie.trailer_url" allowfullscreen></b-embed>
      </b-col>
      <b-col>
        <div class="pt-3">
          <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }} | </span>
          <span>{{ movie.grade }} |</span>
          <span>
            네이버 :
            <span class="badge badge-success">{{ movie.naver_score }}</span>
          </span>
        </div>
        <div>
          <span class="font-weight-bold">감독 : </span>
          <span>{{director_list.join(', ')}}</span>
          <span> | </span>
          <span class="font-weight-bold">배우 : </span>
          <span>{{ actor_list.join(', ')  }}</span>
        </div>
          <hr class="select" />
        <div class="pt-4">
          <h3 >줄거리</h3>
          <p class="pt-4">{{ movie.summary }}</p>
        </div>
      </b-col>
    </b-row>
    <hr class="select mx-3" />
    <h4 class="mx-4">Review</h4>
    <b-row class="justify-content-center mx-5 mt-3">
      <b-col>
        <div class="form-group">
          <label for="comment">Comment</label>
          <input
            type="text"
            id="comment"
            class="form-control"
            placeholder="   코멘트를 남겨주세요."
            v-model="rating.comment"
          />
        </div>
      </b-col>
      <b-col cols="12" md="auto">
        <div class="form-group">
          <label for="comment">Score</label>
          <input
            type="number"
            class="form-control"
            placeholder="0"
            v-model="rating.score"
            min="0"
            max="10"
          />
        </div>
      </b-col>
      <b-col col lg="3" align-self="center" class="mt-3">
        <b-button size="sm" class="btn-success" @click="addRating">Add</b-button>
      </b-col>
    </b-row>
    <hr />
    <link
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      rel="stylesheet"
      integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
      crossorigin="anonymous"
    />
    <div id="review-div" class="mb-3 mx-4" v-for="rating in movie.ratings" :key="rating.id">
        <div class="card my-1 col-10">
          <div class="card-body p-0">
            <div class="row">
              <div class="col-2">
                <p
                  class="text-secondary text-center pt-3"
                >{{ rating.created_at.substr(5, 5).replace('-', '/') }} {{ rating.created_at.substr(11,5)}}</p>
              </div>
              <div class="col-10 pl-0 review-content">
                <p>
                  <a class="float-left my-2">
                    <strong style="font-size:2rem;">{{rating.username}}</strong>
                  </a>
                  <span class="float-right" v-for="i in rating.score" :key="i">
                    <i class="text-warning fa fa-star"></i>
                  </span>
                </p>
                <div class="clearfix"></div>
                <p>{{ rating.comment }}</p>
                <div class="float-right">
                <img
                  v-if="userId === rating.user"
                  class="btn mx-auto mb-2 position-relative"
                  src="@/assets/images/delete_rating.png"
                  alt="delete"
                  style="cursor:pointer;"
                  @click="deleteRating(rating.id)"
                />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import axios from "axios";
import router from "@/router";
export default {
  name: "MovieDetailPage",
  props: {
    movie: {
      type: Object,
      required: true
    },
    director_list: {
      type: Array,
      required: true
    },
    actor_list: {
      type: Array,
      required: true
    },
    likeBool: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      rating: {
        comment: "",
        score: 0.0,
      }
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  methods: {
    goBack() {
      router.go(-1);
    },
    movie_like() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(
          `${SERVER_IP}/api/v1/movies/${this.movie.id}/unlike_like/${this.userId}/`,
          this.options
        )
        .then(response => {
          console.log(response.data);
          this.$emit('likeUnlike', this.likeBool ? false : true);
        })
        .catch(error => {
          console.log(error);
        });
    },
    addRating() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      if (this.rating.score > 10){
        this.rating.score = 10
      }
      axios
        .post(
          `${SERVER_IP}/api/v1/movies/rating_add/`,
          {
            comment: this.rating.comment,
            score: this.rating.score,
            user_id: this.userId,
            movie_id: this.movie.id
          },
          this.options
        )
        .then(response => {
          response.data;
          this.movie.ratings.unshift(response.data);
          this.rating.comment = "";
          this.rating.score = 0;
        })
        .catch(error => {
          console.log(error);
        });
    },
    deleteRating(rating_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .delete(`${SERVER_IP}/api/v1/rating_delete/${rating_id}/`, this.options)
        .then(response => {
          console.log(response.data);
          const itemToFind = this.movie.ratings.find(function(item) {
            return item.id === rating_id;
          });
          const idx = this.movie.ratings.indexOf(itemToFind);
          if (idx > -1) this.movie.ratings.splice(idx, 1);
        })
        .catch(error => {
          console.log(error);
        });
    },
    checklikeBool(){
      return this.likeBool ? true : false
    }
  },
  created(){
  }
};
</script>
<style>
hr.select {
  border: solid 2px white;
}
.review-content{
  color: black;
}
</style>
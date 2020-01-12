<template>
  <div class="py-3 px-5">
    <link
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      rel="stylesheet"
      integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
      crossorigin="anonymous"
    />
    <div v-if="sortRatings.length === 0" class="text-center noneMovie">
      작성한 Comment가 없습니다.
    </div>
    <div id="review-div" v-for="rating in sortRatings" :key="rating.id" class="my-2 mx-5" style="padding-bottom: 30%;">
      <div class="card">
        <div class="card-body">
          <div class="row">
            <div class="col-md-2">
              <h4 class="font-weight-bold text-center my-2">{{rating.movietitle}}</h4>
              <br />
              <p
                class="text-secondary text-center"
              >{{ rating.created_at.substr(5, 5).replace('-', '/') }} {{ rating.created_at.substr(11,5)}}</p>
            </div>
            <div class="col-md-10 my-2 text-dark">
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
                <div class="float-right"></div>
              <b-button
                variant="success"
                class="float-right"
                @click="goDetail(rating.movie)"
              >해당 영화Page 가기</b-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import router from "@/router";
export default {
  name: "UserRatings",
  props: {
    userRatingsList: {
      type: Array,
      required: true
    }
  },
  computed: {
    sortRatings() {
      let clone = this.userRatingsList.slice();
      return clone.sort(function(a, b) {
        return a.created_at > b.created_at
          ? -1
          : a.created_at < b.created_at
          ? 1
          : 0;
      });
    }
  },
  methods: {
    goDetail(movie_id) {
      router.push(`/moviedetail/${movie_id}`);
    }
  }
};
</script>

<style>
</style>
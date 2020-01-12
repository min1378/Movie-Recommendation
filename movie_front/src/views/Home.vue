<template>
  <div class="home mx-5 pt-5">
    <h1 class="text-center text-light">Movie List</h1>
    <hr />
    <div id="nav" class="p-0">
      <b-nav pills class="indexbar justify-content-center">
        <b-nav-item class="mx-1" @click="selectTotal">전체</b-nav-item>
        <b-nav-item-dropdown
          class="mx-1"
          id="my-nav-dropdown"
          :text="genreText"
          toggle-class="nav-link-custom"
          right
          v-if="searchBool"
        >
          <b-dropdown-item
            v-for="genre in genres"
            :key="genre.id"
            @click="selectGenre(genre.name)"
          >{{ genre.name }}</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown
          class="mx-1"
          id="my-nav-dropdown"
          text="Search"
          toggle-class="nav-link-custom"
          right
          v-if="searchBool"
        >
          <b-dropdown-item  @click="searchSelect(0)">감독</b-dropdown-item>
          <b-dropdown-item  @click="searchSelect(1)">배우</b-dropdown-item>
          <b-dropdown-item  @click="searchSelect(2)">영화제목</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-form v-if="!searchBool">
          <b-form-input size="sm" class="mr-sm-2" :placeholder="phSearch" v-model="searchText"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit" @click="searching">Search</b-button>
        </b-nav-form>
      </b-nav>
    </div>
    <hr />
    <div class="nav">
      <select class="ml-auto" v-model="sortNm" style="height: 2rem;">
        <option value="0">최신순</option>
        <option value="1">네이버평점순</option>
        <option value="2">좋아요순</option>
      </select>
    </div>
    <MovieList :movies="selectSort" :currentPage="currentPage" />
  </div>
</template>

<script>
import MovieList from "@/components/MovieList";
import axios from "axios";
import { mapGetters } from "vuex";
import router from "@/router";
export default {
  name: "Home",
  data() {
    return {
      currentPage: 1,
      genreText: "장르별",
      origin_movies: [],
      movies: [],
      genres: [],
      sortNm: 0,
      searchBool: true,
      phSearch: "",
      searchText: ""
    };
  },
  computed: {
    // ...A ; A 가 가진 아이템 다 뿌려 / js 문법
    ...mapGetters(["isLoggedIn", "options", "userId"]),
    selectSort: function() {
      let clone = this.movies.slice();
      if (this.sortNm == 1) {
        return clone.sort(function(a, b) {
          return a.naver_score > b.naver_score
            ? -1
            : a.naver_score < b.naver_score
            ? 1
            : 0;
        });
      } else if (this.sortNm == 2) {
        return clone.sort(function(a, b) {
          return a.liked_users.length > b.liked_users.length
            ? -1
            : a.liked_users.length < b.liked_users.length
            ? 1
            : 0;
        });
      } else {
        return clone.sort(function(a, b) {
          return a.opendt > b.opendt ? -1 : a.opendt < b.opendt ? 1 : 0;
        });
      }
    }
  },
  components: {
    MovieList
  },
  methods: {
    getMovies() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/movies/`)
        .then(response => {
          this.movies = response.data;
          this.origin_movies = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getGenres() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/genres/`, this.options)
        .then(response => {
          this.genres = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    selectGenre(value) {
      this.genreText = value;
      this.movies = this.origin_movies.filter(movie => {
        let tempBool = false;
        for (let item of movie.genres) {
          if (item.name === value) {
            tempBool = true;
            break;
          }
        }
        return tempBool;
      });
    },
    selectTotal() {
      this.searchBool = true;
      this.genreText = "장르별";
      this.movies = this.origin_movies;
    },
    searchSelect(value) {
      this.searchBool = false;
      if (value === 0) {
        this.phSearch = "Director Search";
      } else if (value === 1) {
        this.phSearch = "Actor Search";
      } else {
        this.phSearch = "Movie Search";
      }
    },
    searching() {
      this.selectTotal();
      this.searchingBool = true;
      if (!this.searchText.trim()) {
        return;
      }
      if (this.phSearch === "Director Search") {
        this.movies = this.origin_movies.filter(movie => {
          for (let item of movie.directors) {
            return item.name.indexOf(this.searchText.trim()) !== -1;
          }
        });
        this.searchText = "";
      } else if (this.phSearch === "Actor Search") {
        this.movies = this.origin_movies.filter(movie => {
          for (let item of movie.actors) {
            return item.name.indexOf(this.searchText.trim()) !== -1;
          }
        });
        this.searchText = "";
      } else {
        this.movies = this.origin_movies.filter(movie => {
          return movie.title.indexOf(this.searchText.trim()) !== -1;
        });
        this.searchText = "";
      }
    }
  },
  created() {
    if (!this.isLoggedIn) {
      router.push('/login')
    }
    else{
      this.getMovies();
      this.getGenres();
    }
  }
};
</script>

<style>
#nav {
  padding: 0px;
  font-weight: bold;
  color: #2c3e50;
}
#nav li a {
  font-size: 20px;
  color: white;
  background-color:grey
}
#nav li a:hover {
  font-size: 21px;
  color: white;
  background-color: grey;
}
#nav li a:active {
  font-size: 20px;
  color: white;
  background-color: grey;
}
ul.dropdown-menu {
  padding: 0;
}
</style>

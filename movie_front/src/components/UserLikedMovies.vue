<template>
  <div class="mt-3 px-3">
    <div v-if="userLikedMoviesList.length === 0" class="text-center noneMovie">
      좋아요한 영화가 없습니다.
    </div>
    <MovieList v-if="userLikedMoviesList.length !== 0" :movies="userLikedMoviesList" :currentPage="currentPage"/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
export default {
  name: 'UserLikedMovies',
  props:{
    userLikedMoviesList:{
      type:Array,
      required :true
    }
  },
  components:{
    MovieList
  },
  data(){
    return{
      currentPage:1,
    }
  }
}
</script>

<style>
  .noneMovie{
    font-size: 4rem;
    padding-top: 20%;
    padding-bottom: 25%;
  }
</style>
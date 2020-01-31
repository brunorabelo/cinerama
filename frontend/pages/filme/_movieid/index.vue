<template>
  <div>
    <movie-detail v-bind:movie_details="movie_details" v-bind:logged_user="logged_user" />
  </div>
</template>

<script>
import movieDetail from "~/components/movie-detail.vue";
import AppApi from "~apijs";

export default {
  components: {
    "movie-detail": movieDetail
  },
  data() {
    return { movie_id: {}, key: false };
  },
  computed: {
    logged_user() {
      return this.$store.getters.logged_user;
    }
  },
  asyncData(context) {
    const movie_id = context.params.movieid;
    return AppApi.get_movie_details(movie_id).then(result => {
      return {
        movie_details: result.data
      };
    });
  },
  watch: { logged_user: function(newUser, oldUser) {
      
      if(newUser !=null){
        this.$router.go() 
      }
  } }
};
</script>



<style>
</style>

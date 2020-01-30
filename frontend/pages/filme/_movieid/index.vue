<template>
<div>
  <movie-detail :movie_details="movie_details" />
   <div v-if="key">
   </div>
</div>
</template>

<script>
import movieDetail from "~/components/movie-detail.vue";
import AppApi from "~apijs";

export default {
  watchQuery: ['logged_user'],
  components: {
    "movie-detail": movieDetail
  },
  data(){
    return {
      key :false
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
  
  computed: {
    logged_user() {
      return this.$store.getters.logged_user;
    }
  }

  
};
</script>



<style>
</style>

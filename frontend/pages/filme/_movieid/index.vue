<template>
  <div>
    <movie-detail :movie_details="movie_details" />
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
    return {
    };
  },
  asyncData(context) {
    const movie_id = context.params.movieid;
    return AppApi.get_movie_details(movie_id).then(result => {
      return {
        movie_details: result.data
      };
    });
  }
};
</script>



<style>
</style>

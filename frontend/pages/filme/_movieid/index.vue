<template>
    <movie-detail :movie_details="movie_details"/>  
</template>

<script>

import movieDetail from '~/components/movie-detail.vue'
import AppApi from '~apijs'


export default {
    components: {
    'movie-detail':movieDetail
    },
    asyncData (context){
        const movieid = context.params.movieid
        return AppApi.get_movie_details(movieid).then(
         result => {
           
        return {
          movie_details: result.data
        }
      }
    )
    },
    data () {
        return {
            
        }
  }
}
</script>



<style>
</style>

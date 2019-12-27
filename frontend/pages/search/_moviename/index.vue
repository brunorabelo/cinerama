<template>
    <movie-search-list :movie_list="movie_list"/>  
</template>

<script>

import movieSearchList from '~/components/movie-search-list.vue'
import AppApi from '~apijs'


export default {
    components: {
    'movie-search-list':movieSearchList
    },
    asyncData (context){
        const moviename = context.params.moviename
        return AppApi.get_movies_search_result(moviename).then(
         result => {
           
        return {
          movie_list: result.data
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

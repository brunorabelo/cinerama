<template>
    <movie-list  :movie_list="movie_list"/>  
</template>

<script>

import movieList from '~/components/movie-list.vue'
import AppApi from '~apijs'

export default {
    components: {
        'movie-list':movieList
    },
    asyncData (context){
      
        const username = context.params.username
        debugger
        return AppApi.get_movie_list(username).then(
         result => {
           debugger
        return {

          movie_list: result.data['movies']
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

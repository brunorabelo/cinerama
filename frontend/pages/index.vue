<template>
<div>
  <h1 align="center">Filmes em Cartaz</h1>
<home :movies="movie_list" v-if="movie_list"></home>
</div>
</template>

<script>

import home from '~/components/Home.vue'
import AppApi from '~apijs'



export default {
  components:{
    home
  },
  asyncData(){

    return AppApi.list_movies_now_playing().then(
      result => {
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

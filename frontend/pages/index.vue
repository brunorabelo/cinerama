<template>
<div>
  <h1>Filmes em Cartaz</h1>
<home :movies="movies" v-if="movies"></home>
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
          movies: result.data
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

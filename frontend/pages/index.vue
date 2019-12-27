<template>
<div>

  <v-row justify="center" align="center"
          v-if="!movies">
  
     <div class="text-center ma-12">
  <v-progress-circular 
          :indeterminate = "true"
          :size=200
          :value=0
          :width=5
          color="light-blue"
        ></v-progress-circular>
     </div>
  </v-row>
  <v-row>
  <home :movies="movies" v-if="movies"></home>
  </v-row>
</div>
</template>

<script>

import home from '~/components/Home.vue'
import AppApi from '~apijs'

export default {
  components:{
    home
  },
  data () {
    return {
      movies:null,
    }
  },
  mounted(){
    AppApi.list_movies_now_playing().then(result=>{
      this.movies=result.data
    })
  }
}
</script>

<style>
</style>

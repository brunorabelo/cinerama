<template>
<v-carousel
    height="600"
    hide-delimiter-background
    show-arrows-on-hover
  >
  <router-link v-for="(movie,i) in movies"
      :key="i" 
      :to="{name:'filme-movieid',params:{movieid:movie.id}}"
      
      tag="a">
    
    <v-carousel-item
      
      :src="movie.backdrop_path"
      
      reverse-transition="fade-transition"
      transition="fade-transition"
    >
     <v-responsive dark height="95%" >
            <v-container fill-height>
              <v-layout align-end>
                <v-flex>
                  <h3 class="display-3 white--text">{{movie.title}}</h3>
                  <!-- <span class="subheading white--text">Subtítulo filme {{ i + 1}}</span> -->
                </v-flex>
              </v-layout>
            </v-container>
          </v-responsive>
    </v-carousel-item>
  </router-link>
  </v-carousel>
</template>


<script>
export default {
  props: ['movies']
}
</script>

<style>

</style>
<template>
<v-carousel
    height="600"
    hide-delimiter-background
    show-arrows-on-hover
  >
    <v-carousel-item
      v-for="(movie,i) in movies"
      :key="i"
      :src="movie.backdrop_path"
      
      reverse-transition="fade-transition"
      transition="fade-transition"
    >
     <v-responsive dark height="95%" >
            <v-container fill-height>
              <v-layout align-end>
                <v-flex>
                  <h3 href="/test.html" class="display-3 white--text">{{movie.title}}</h3>
                  <!-- <span class="subheading white--text">Subtítulo filme {{ i + 1}}</span> -->
                </v-flex>
              </v-layout>
            </v-container>
          </v-responsive>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data () {
      return {
        movies: [
          {
            poster_path: "http://image.tmdb.org/t/p/original/e1mjopzAS2KNsvpbpahQ1a6SkSn.jpg",
            id: 297761,
            backdrop_path:"http://image.tmdb.org/t/p/original/ndlQ2Cuc3cjTL7lTynw6I4boP4S.jpg",
            title: "Suicide Squad", 
          },  
          {
            poster_path: "http://image.tmdb.org/t/p/original/3ioyAtm0wXDyPy330Y7mJAJEHpU.jpg",
            id: 328387,
            title: "Nerve",
            backdrop_path: "http://image.tmdb.org/t/p/original/a0wohltYr7Tzkgg2X6QKBe3txj1.jpg",
          },
          
          {
            poster_path: "http://image.tmdb.org/t/p/original/3S7V2Jd2G61LltoCsYUj4GwON5p.jpg",
            id: 376659,
            title: "Bad Moms",
            backdrop_path: "http://image.tmdb.org/t/p/original/l9aqTBdafSo0n7u0Azuqo01YVIC.jpg",
            },
        ],
      }
    },
  }
</script>

<style>

</style>
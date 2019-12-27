<template>

  <v-card
  :loading="loading"
    class="mx-auto my-12"
    max-width="374" 
  >
    <v-img
    height="250"
      :src="movie_details.backdrop_path"
    ></v-img>

    <v-card-title class=" mx-0 display-1 font-weight-black	" >{{movie_details.title}}</v-card-title>
    <v-card-text>
      <v-row 
      align="left" class="mx-0">
      <div class="ma-0 subtitle-1 black--text">
        <v-icon>event</v-icon>  {{movie_details.release_date}}
      </div>
      </v-row>
      <div class="my-4">{{movie_details.overview}} </div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Sua avaliação:</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value=movie_details.user_rating
          color="amber"
          dense
          clearable="true"
          half-increments
          size="40"
        ></v-rating>

      </v-row>

    </v-card-text>

    <v-card-actions>
      <v-btn
        
        color="deep-purple accent-4"
        text
        @click="reserve"
      >
        Salvar
      </v-btn>
    </v-card-actions>
  </v-card>
</template>



<script>
  export default {
    name: 'movieDetail',
  props: ['movie_details'],
  data: () => ({
      loading: false,
      selection: 1,
    }),

    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
    },
  }

  
</script>

<style>

</style>
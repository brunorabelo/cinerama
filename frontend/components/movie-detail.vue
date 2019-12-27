<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-img :src="movie_details.backdrop_path" height="100%">
        </v-img>
        <v-card-title primary-title>
          <div>
            <h3 class="headline mb-0">{{movie_details.title}}</h3>

      <v-card-text>
        <v-icon>event</v-icon>
        {{movie_details.release_date}}
      </v-card-text>
            <div>{{movie_details.overview}}</div>
          </div>
        </v-card-title>
        <v-divider class="mx-4"></v-divider>


        <v-card-text>
          Sua avaliação:
        <v-rating
          :value=movie_details.user_rating
          color="amber"
          dense
          :clearable="true"
          half-increments
          size="40"
        ></v-rating>
    </v-card-text>
        <v-card-actions>
          <v-btn flat color="orange">Salvar</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
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
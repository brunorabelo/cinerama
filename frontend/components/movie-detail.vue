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

        <div v-if="logged_user">
          <v-form ref='form' :key="componentKey">
        <v-card-text>
          Sua avaliação:
        <v-rating
          v-model="rating_input"
          :value=movie_details.user_rating
          color="amber"
          dense
          :clearable="true"
          half-increments
          size="40"
        ></v-rating>
    </v-card-text>
        <v-card-actions>
          <v-btn :loading='loading' flat color="orange" @click.native="save_rating()">Salvar</v-btn>
        </v-card-actions>
          </v-form>
        </div>
      </v-card>
    </v-flex>
     <v-snackbar
      :timeout="6000"
      color="success"
      v-model="snackbar"
    >
      {{ snack_text }}
      <v-btn flat color="pink" @click.native="snackbar = false">Close</v-btn>
    </v-snackbar>
  </v-layout>
  
</template>





<script>
import AppApi from '~apijs'

import Snacks from '~/helpers/Snacks.js'

  export default {
    name: 'movieDetail',
  props: ['movie_details'],
  data () {
    return {
      componentKey: 0,
      loading:false,
      rating_input:this.movie_details.user_rating,
      snack_text:'',
      snackbar:false
    }
  },
  computed:{
      logged_user(){
        return this.$store.getters.logged_user
      }
  },
    methods: {
      reserve () {

        setTimeout(() => (this.loading = false), 2000)
      },
      save_rating(){
        this.loading = true

        this.rating_info= {
          user_rating:this.rating_input,
          movie_id:this.movie_details.id
        }

        const self = this

         AppApi.save_rating(this.rating_info).then(()=>
            {
              this.loading=false
              this.snackbar=true
              this.snack_text="Salvo com sucesso!"
              
            }) 

 
      }
    },
  }

  
</script>

<style>

</style>
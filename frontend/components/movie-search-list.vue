<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-toolbar color="cyan" dark>
            <v-icon>search</v-icon>
          <v-toolbar-title>Busca</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-list three-line>
          <template v-for="(item, index) in movie_list">
            <v-subheader v-if="item.header" :key="item.header">{{ item.header }}</v-subheader>
            <v-divider v-else-if="item.divider" :inset="item.inset" :key="index"></v-divider>
            <v-list-tile v-else :key="index" avatar :to="{name:'filme-movieid',params:{movieid:item.id}}">
              <v-list-tile-avatar tile>
                <img :src="item.backdrop_path">
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title v-html="item.title"></v-list-tile-title>
                <v-list-tile-sub-title v-html="item.release_date"></v-list-tile-sub-title>
                <v-list-tile-sub-title v-html="item.overview"></v-list-tile-sub-title>
                
              </v-list-tile-content>
            </v-list-tile>
          </template>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
</template>



<script>
  export default {
           props: ['movie_list'],   
    data () {
      return {
      }
    }
  }
</script> 

<style>

</style>
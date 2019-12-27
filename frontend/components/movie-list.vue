<template>
<div>
  <h1 class="display1 pa-2">Seus filmes</h1>
  <v-data-table
    :headers='headers'
    :items='movie_list'
    hide-actions
    class="elevation-1"
  >
    <template slot="items" slot-scope="props" :to="{name: 'index'}">
      
      <td><router-link :to="{name: 'filme-movieid', params:{movieid:props.item.id}}"> {{ props.item.title }}</router-link></td>
      <td class="text-xs-right">{{ props.item.release_date }}</td>
      <td class="text-xs-right">{{ props.item.user_rating }}</td>
      
    </template>
  </v-data-table>
</div>
</template>

<script>
  export default {
           props: ['movie_list'],    
data () {
      return {
        headers: [
          {
            text: 'Filme',
            align: 'left',
            sortable: true,
            value: 'name'
          },
          { text: 'Ano', value: 'year' },,
          { text: 'Nota', value: 'rating' }
        ],
      }
    },
  }
</script>

<style>

</style>
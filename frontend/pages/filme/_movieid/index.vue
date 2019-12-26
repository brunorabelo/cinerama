<template>
    <h1>Página do filme {{movieid}}</h1>  
</template>

<script>

export default {
    asyncData (context){
        return{
            movieid: context.params.movieid
        }
    },
    data () {
        return {}
  }
}
</script>

<style>
</style>

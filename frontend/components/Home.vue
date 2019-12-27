<template>
    <moviecarousel :movies="movies"></moviecarousel>
</template>

<script>

import moviecarousel from '~/components/moviecarousel.vue'

export default {
    props: ['movies'],
    components:{
        moviecarousel
    },
    data(){
        return{}
    }
}
</script>

<style>

</style>
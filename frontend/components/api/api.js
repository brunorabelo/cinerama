import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        return post('/api/login', {username: username, password: password});
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    add_todo(newtask){
        return post('/api/add_todo', {new_task: newtask});
    },
    list_todos(){
        return get('/api/list_todos');
    },
    list_movies_now_playing(){
        return get('/api/list_movies_now_playing');
    },

    get_movie_details(movieid){
        return get('api/get_movie_details',{movie_id:movieid});
    },

    get_movie_list(user){
        return get('api/get_movie_list',{user:user});
    },
    get_movies_search_result(moviename){
        return get('api/get_movies_search_result',{movie_search:moviename});
    },
    save_rating(rating_info){
        return post('api/save_rating',{rating_info:rating_info});
    },


}
export default api;

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}

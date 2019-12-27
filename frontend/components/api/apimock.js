import Vue from 'vue'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(username, password){
        if(password){
            logged_user = {
                username: username,
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: username == 'admin',
                    STAFF: username == 'admin',
                }
            };
        }
        return mockasync(logged_user);
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },
    add_todo(newtask){
        return mockasync({description: newtask, done: false});
    },
    list_todos(){
        return mockasync({
            todos: [
                {description: 'Do the laundry', done: true},
                {description: 'Walk the dog', done: false}
            ]
        });
    },
    list_movies_now_playing(){
        return mockasync([
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
                  }
              ]); 
        
    }
};

export default api;

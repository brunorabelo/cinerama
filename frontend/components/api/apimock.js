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
    list_movies_now_playing(){
        return mockasync({movies:[
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
              ]}); 
        
    },

    get_movie_details(movie_id){
        

        return mockasync(movie_id==550?{
            
            poster_path: "http://image.tmdb.org/t/p/original/8pcOlY6jaupFKTIy2aeKCKZ2GMj.jpg",
            id: 550,
            backdrop_path:"http://image.tmdb.org/t/p/original/mMZRKb3NVo5ZeSPEIaNW9buLWQ0.jpg",
            title: "Fight Club",
            overview: "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
            release_date: "1999-10-12",
            user_rating: null,
    
        }:{
            
            poster_path: "http://image.tmdb.org/t/p/original/8pcOlY6jaupFKTIy2aeKCKZ2GMj.jpg",
            id: 550,
            backdrop_path:"http://image.tmdb.org/t/p/original/mMZRKb3NVo5ZeSPEIaNW9buLWQ0.jpg",
            title: "Fight Club",
            overview: "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
            release_date: "1999-10-12",
            user_rating: 4.0,

        });
    },

    get_movie_list(user){

        return mockasync(
            {movies:[                
                {
                  id: 19404,
                  title: "Dilwale Dulhania Le Jayenge",
                  user_rating: 3.5,
                  poster_path: "http://image.tmdb.org/t/p/original/2CAL2433ZeIihfX1Hb2139CX0pW.jpg",
                  backdrop_path: "http://image.tmdb.org/t/p/original/pVGzV02qmHVoKx9ehBNy7m2u5fs.jpg",
                  overview: "Raj is a rich, carefree, happy-go-lucky second generation NRI. Simran is the daughter of Chaudhary Baldev Singh, who in spite of being an NRI is very strict about adherence to Indian values. Simran has left for India to be married to her childhood fiancé. Raj leaves for India with a mission at his hands, to claim his lady love under the noses of her whole family. Thus begins a saga.",
                  release_date: "1995-10-20"
                },
                {
                  poster_path: "http://image.tmdb.org/t/p/original/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
                  id: 278,
                  backdrop_path: "http://image.tmdb.org/t/p/original/j9XKiZrVeViAixVRzCta7h1VU9W.jpg",
                  title: "The Shawshank Redemption",
                  overview: "Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
                  release_date: "1994-09-23",
                  user_rating: 4.5
                },
                {
                  id: 238,
                  title: "The Godfather",
                  release_date: "1972-03-14",
                  backdrop_path: "http://image.tmdb.org/t/p/original/6xKCYgH16UuwEGAyroLU6p8HLIn.jpg",
                  overview: "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
                  poster_path: "http://image.tmdb.org/t/p/original/rPdtLWNsZmAtoZl9PK7S2wE3qiS.jpg",
                  user_rating: 5.0
                },
                {
                  poster_path: "http://image.tmdb.org/t/p/original/yPisjyLweCl1tbgwgtzBCNCBle.jpg",
                  id: 424,
                  backdrop_path: "http://image.tmdb.org/t/p/original/cTNYRUTXkBgPH3wP3kmPUB5U6dA.jpg",
                  title: "Schindler's List",
                  overview: "The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II.",
                  release_date: "1993-11-30",
                  user_rating: 4.0
                },
                
            ]});
    },
    get_movies_search_result(moviename){
        return mockasync(
          {movies:            [
                {
                  poster_path: "http://image.tmdb.org/t/p/original/4KvrvcqckdupXXO2YnANtyG7QLK.jpg",
                  id: 1598,
                  backdrop_path: "http://image.tmdb.org/t/p/original/zDVrWS9PzI0HJU1kyfO6UNsx9br.jpg",
                  title: "Cape Fear",
                  overview: "Sam Bowden is a small-town corporate attorney. Max Cady is a tattooed, cigar-smoking, bible-quoting, psychotic rapist. What do they have in common? Fourteen years ago, Sam was a public defender assigned to Max Cady's rape trial, and he made a serious error: he hid a document from his illiterate client that could have gotten him acquitted. Now, the cagey, bibliophile Cady has been released, and he intends to teach Sam Bowden and his family a thing or two about loss.",
                  release_date: "1991-11-15"
                },
                {
                  poster_path: "http://image.tmdb.org/t/p/original/reA4wlTY9qGwryVftscFT2q0ZLK.jpg",
                  id: 10543,
                  backdrop_path: "http://image.tmdb.org/t/p/original/yBQFqrRyvf7WrmEDAzrny982uDJ.jpg",
                  title: "Fear",
                  overview: "A 16 year old girl takes up with a charming young man who quickly shows his colors when he beats a friend simply for walking with her and then goes totally ballistic after she tries to break up with him.",
                  release_date: "1996-04-12"
                },
                {
                  id: 392058,
                  title: "Fear, Inc.",
                  release_date: "2016-04-15",
                  backdrop_path: "http://image.tmdb.org/t/p/original/A5rCoD620Eg8jqotGEWXdBl1UDY.jpg",
                  overview: "Horror junkie Joe Foster gets to live out his ultimate scary movie fantasy courtesy of Fear Inc., a company that specializes in giving you the fright of your life. But as lines blur between what is and is not part of the game, Joe's dream come true begins to look more like a nightmare.",
                  poster_path: "http://image.tmdb.org/t/p/original/mbsX8ZynHg6FoD1Pt6j2jCRAZBu.jpg"
                },
            ]   
          });
    },


    save_rating(rating_info){
      return mockasync({
        
      });
    }



};

export default api;

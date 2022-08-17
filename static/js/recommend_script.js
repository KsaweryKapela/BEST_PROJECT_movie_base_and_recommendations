recommendImage = document.getElementById('recommend-image');

recommendHeart = document.getElementById('recommend-heart');
recommendBookmark = document.getElementById('recommend-bookmark');
recommendDislike = document.getElementById('recommend-dislike');
recommendIgnore = document.getElementById('recommend-ignore');


[recommendHeart, recommendBookmark, recommendDislike, recommendIgnore]
.forEach(element => element.addEventListener('click', recommendIconClick));


async function recommendIconClick(){
await fetchData('edit_user_lists', index=0, command = 'recAdd', command2=this.id.substring(20, 10))
loadRecommendation();
}

loadRecommendation();

async function loadRecommendation() {
    const recommendation_json = await fetchRecommendations();
    recommendImage.src = recommendation_json['movie_url'];
    document.getElementsByClassName('rm-movie-title')[0].textContent = recommendation_json['movie_title'];
    document.getElementsByClassName('rm-date-runtime-PG')[0].textContent = recommendation_json['movie_date'];
    document.getElementsByClassName('rm-date-runtime-PG')[0].textContent += ' | ' + recommendation_json['movie_runtime'];
    document.getElementsByClassName('rm-date-runtime-PG')[0].textContent += ' | ' + recommendation_json['movie_pg'];
    document.getElementsByClassName('rm-genres')[0].textContent = recommendation_json['movie_genre'];
    document.getElementsByClassName('rm-director')[0].textContent = 'by ' + recommendation_json['movie_director'];
    document.getElementsByClassName('rm-writer')[0].textContent = 'Screenplay: ' + recommendation_json['movie_writer'];
    document.getElementsByClassName('rm-description')[0].textContent = recommendation_json['movie_description'];
    document.getElementsByClassName('rm-cast')[0].textContent = 'main cast: ' + recommendation_json['movie_cast'].slice(0, -2);
    document.getElementsByClassName('rm-tomatometer')[0].textContent = recommendation_json['movie_tomatometer'];
    document.getElementsByClassName('rm-audience')[0].textContent = recommendation_json['movie_audience'];
    document.getElementsByClassName('rm-studio-boxoffice')[0].textContent = 'Produced by ' + recommendation_json['movie_studio']
  + ' | US boxoffice: $' + recommendation_json['movie_boxoffice'];



    }

async function fetchRecommendations() {
    response = await fetch('/fetch_recommend');
    const raw_data = await response.json();
    return raw_data;
};
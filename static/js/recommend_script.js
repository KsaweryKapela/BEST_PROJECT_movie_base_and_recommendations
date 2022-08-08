recommendImage = document.getElementById('recommend-image');

recommendHeart = document.getElementById('recommend-heart');
recommendBookmark = document.getElementById('recommend-bookmark');
recommendDislike = document.getElementById('recommend-dislike');
recommendIgnore = document.getElementById('recommend-ignore');


[recommendHeart, recommendBookmark, recommendDislike, recommendIgnore]
.forEach(element => element.addEventListener('click', recommendIconClick));


async function recommendIconClick(){
await fetchData('edit_user_lists', index=0, command = 'recAdd', command2=this.id.substring(20, 10))
const recommendation_url = await fetchRecommendations();
recommendImage.src = recommendation_url['movie_url'];
}

loadRecommendation();

async function loadRecommendation() {
    const recommendation_url = await fetchRecommendations();
    recommendImage.src = recommendation_url['movie_url'];
    }


async function fetchRecommendations() {
    response = await fetch('/fetch_recommend');
    const raw_data = await response.json();
    return raw_data;
};
recommendImage = document.getElementById('recommend-image');

recommendHeart = document.getElementById('recommend-heart');
recommendBookmark = document.getElementById('recommend-bookmark');
recommendDislike = document.getElementById('recommend-dislike');
recommendIgnore = document.getElementById('recommend-ignore');


[recommendHeart, recommendBookmark, recommendDislike, recommendIgnore]
.forEach(element => element.addEventListener('click', recommendIconClick));

index = 0;


async function recommendIconClick(){
fetchData('edit_user_lists', index, command = 'recAdd', command2=this.id.substring(20, 10))
const recommendation_url = await fetchRecommendations();
console.log(recommendation_url['movie_url'])
recommendImage.src = recommendation_url['movie_url'];
index += 1;
}

loadRecommendation();

async function loadRecommendation() {
    const recommendation_url = await fetchRecommendations();
    console.log(recommendation_url['movie_url'])
    recommendImage.src = recommendation_url['movie_url'];
    index += 1;
    }


async function fetchRecommendations() {
    response = await fetch('/fetch_recommend' + '?' + new URLSearchParams(
    {'index': index,
    }));
    const raw_data = await response.json();
    console.log(raw_data);
    return raw_data;
};
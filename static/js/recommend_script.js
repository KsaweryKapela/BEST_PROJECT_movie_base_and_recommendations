recommendImage = document.getElementById('recommend-image');

async function fetchRecommendations() {
    response = await fetch('/fetch_recommend' + '?' + new URLSearchParams(
    {'index': index,
    }));
    const raw_data = await response.json();
    console.log(raw_data);
    return raw_data;
};

index = 0;

loadRecommendation();
recommendImage.addEventListener('click', loadRecommendation);

console.log(recommendImage);

async function loadRecommendation() {
    const recommendation_url = await fetchRecommendations();
    console.log(recommendation_url['movie_url'])
    recommendImage.src = recommendation_url['movie_url'];
    index += 1;
    }

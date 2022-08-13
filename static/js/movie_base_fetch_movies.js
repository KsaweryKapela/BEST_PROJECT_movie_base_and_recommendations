genres = []
order = ''
rating = ''
critics = ''
audience = ''


async function loadMovies() {

    placeArrows();

    const url_list = await fetchMovieBase();
    inputBox.setAttribute('value', url_list['key']);
    recognizeIconState(url_list);

    for (x = 0; x < 4; x++) {

        if (url_list['movie_url'][x] == undefined){
        cardButtons[x].style.visibility = "hidden";
        rightArrow.style.visibility = "hidden";
        img[x].style.visibility = "hidden";

        }else{
        rightArrow.style.visibility = "visible";
        cardButtons[x].style.visibility = "visible";
        printCard(x, url_list)}

        if (url_list['movie_url'][4] == undefined)
        {rightArrow.style.visibility = "hidden";}}}



async function fetchMovieBase() {
    response = await fetch('fetch_moviebase' + '?' + new URLSearchParams(
    {'search': search,
    'index': movieIndex,
    'order': order,

    'genres': genres,
    'rating': rating,
    'critics': critics,
    'audience': audience,
    'key': inputBox.value,
    }));
    const raw_data = await response.json();
    return raw_data;
}

async function fetchData(url, data, command, command2='cmd') {
    response = await fetch(url + '?' + new URLSearchParams(
    {'value': data,
    'command': command,
    'command2': command2
    }));
    const raw_data = await response.json();
    return raw_data;
}
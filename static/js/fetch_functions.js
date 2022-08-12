async function fetchData(url, data, command, command2='cmd') {
    response = await fetch(url + '?' + new URLSearchParams(
    {'value': data,
    'command': command,
    'command2': command2
    }));
    const raw_data = await response.json();
    return raw_data;
}

async function fetchRequest(url) {
    response = await fetch(url)
    const raw_data = await response.json();
    return raw_data;
}

async function fetchMovies(hits, rotten, liked, new_, certified) {
    response = await fetch('fetch_moviebase' + '?' + new URLSearchParams(
    {'index': movie_index,
    'hits': hits,
    'key': userData,
    'rotten': rotten,
    'liked': liked,
    'new': new_,
    'certified': certified,
    'search': search,
    'key': inputBox.value
    }));
    const raw_data = await response.json();
    return raw_data;
}


async function loadMovies(hits=null, rotten=null, liked=null, new_=null, certified=null) {


    placeArrows();

    const url_list = await fetchMovies(hits, rotten, liked, new_, certified);
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

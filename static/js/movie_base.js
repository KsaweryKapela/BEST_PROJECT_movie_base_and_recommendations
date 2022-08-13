movieIndex = 0;
x = selectItem.bind(orderByElements[0]);
x();

loadMovies();



function printCard(x, movieData){


imgDiv[x].addEventListener('mouseover', showDisplay.bind(x))
imgDiv[x].addEventListener('mouseleave', deleteDisplay.bind(x))
imgDiv[x].addEventListener('mouseleave', showFront.bind(this, x));


img[x].addEventListener("click", showBack.bind(this, x, {once:true}));

img[x].src = movieData['movie_url'][x]
img[x].style.visibility = "visible";

dtTitle[x].textContent = movieData['movie_title'][x]

if(dtTitle[x].textContent.length > 19){
dtTitle[x].style.fontSize = "1vw";
}else{dtTitle[x].style.fontSize = "1.3vw";}
dtDescription[x].textContent = movieData['movie_description'][x]
dtDate[x].textContent = movieData['movie_date'][x]
dtStudio[x].textContent = movieData['movie_studio'][x]
dtTomatometer[x].textContent = movieData['movie_tomatometer'][x]
dtAudience[x].textContent = movieData['movie_audience'][x]
dtDirector[x].textContent = movieData['movie_director'][x]
dtGenres[x].textContent = movieData['movie_genre'][x]
dtBoxoffice[x].textContent = movieData['movie_boxoffice'][x]
}

function showBack(x){
img[x].classList.add('blur')
document.getElementsByClassName('db-movie-back')[x].style.visibility = "visible";
}


function showFront(x){
img[x].classList.remove('blur')
document.getElementsByClassName('db-movie-back')[x].style.visibility = "hidden";
}

function showDisplay(){
cardButtons[this].classList.add('visible');
}

function deleteDisplay(){
cardButtons[this].classList.remove('visible');
}

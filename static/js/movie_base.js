movie_index = 0;

loadMovies();

disableSwitches();

freshCheck.addEventListener("click", checkForSwitches);


function printCard(x, movieData){
img[x].src = movieData['movie_url'][x]
img[x].style.visibility = "visible";

dtTitle[x].textContent = movieData['movie_title'][x]

if(dtTitle[x].textContent.length > 19){
dtTitle[x].style.fontSize = "1rem";
}else{dtTitle[x].style.fontSize = "1.3rem";}
dtDescription[x].textContent = movieData['movie_description'][x]
dtDate[x].textContent = movieData['movie_date'][x]
dtStudio[x].textContent = movieData['movie_studio'][x]
dtTomatometer[x].textContent = movieData['movie_tomatometer'][x]
dtAudience[x].textContent = movieData['movie_audience'][x]
dtDirector[x].textContent = movieData['movie_director'][x]
dtGenres[x].textContent = movieData['movie_genre'][x]
dtBoxoffice[x].textContent = movieData['movie_boxoffice'][x]

img[x].addEventListener("click", showBack.bind(this, x, {once:true}));}

function showBack(x){
cardButtons[x].style.visibility = "hidden";
img[x].classList.add('blur')
document.getElementsByClassName('db-movie-back')[x].style.visibility = "visible";
img[x].addEventListener('mouseleave', showFront.bind(this, x), {once:true});
}


function showFront(x){
cardButtons[x].style.visibility = "visible";
img[x].classList.remove('blur')
document.getElementsByClassName('db-movie-back')[x].style.visibility = "hidden";
}

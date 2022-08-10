choseSearch = document.getElementById("chose-search")
inputBox = document.getElementById("db-search-input");
userData = ''
search = 'title';
clicks = 1;

inputBox.onkeyup = (e)=>{
    movie_index = 0;
    userData = e.target.value;
    loadMovies();}

choseSearch.addEventListener('click', swapSearch)

function swapSearch() {
inputBox.value = '';
movie_index = 0;
loadMovies();

if(clicks==0){
inputBox.placeholder = 'Enter title';
search = 'title';
clicks += 1}
else if(clicks==1){
inputBox.placeholder = 'Enter collection';
search = 'collection';
clicks += 1}
else if(clicks==2){
inputBox.placeholder = 'Enter director';
search = 'director';
clicks += 1}
else if(clicks==3){
inputBox.placeholder = 'Enter distributor';
search = 'studio';
clicks += 1}
else if(clicks==4){
inputBox.placeholder = 'Enter actor name';
search = 'cast';
clicks = 0}
checkForSwitches()};
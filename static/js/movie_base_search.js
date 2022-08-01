choseSearch = document.getElementById("chose-search")
inputBox = document.getElementById("db-search-input");
userData = ''
search = 'title';
clicks = 1;

inputBox.onkeyup = (e)=>{
    movie_index = 0;
    userData = e.target.value;
    checkForSwitches();}

choseSearch.addEventListener('click', swapSearch)

function swapSearch() {
if(clicks==0){
inputBox.placeholder = 'Sort by title';
search = 'title';
clicks += 1}
else if(clicks==1){
inputBox.placeholder = 'Sort by collection';
search = 'collection';
clicks += 1}
else if(clicks==2){
inputBox.placeholder = 'Sort by director';
search = 'director';
clicks += 1}
else if(clicks==3){
inputBox.placeholder = 'Sort by studio';
search = 'studio';
clicks += 1}
else if(clicks==4){
inputBox.placeholder = 'Sort by cast';
search = 'cast';
clicks = 0}
checkForSwitches()};
var dropdowns = document.getElementsByClassName('order-by');

orderByElements = dropdowns[0].getElementsByClassName('order-item');
genresElements = dropdowns[1].getElementsByClassName('order-item');
ratingElements = dropdowns[2].getElementsByClassName('order-item');
criticsElements = dropdowns[3].getElementsByClassName('order-item');
audienceElements = dropdowns[4].getElementsByClassName('order-item');



for (let dropdown of dropdowns) {
    dropdown.addEventListener('click', dropTheBar);
    dropdown.addEventListener('mouseleave', hideTheBar);
}

function dropTheBar(){
this.getElementsByClassName('order-by-content')[0].classList.add('enabled');
}

function hideTheBar(){
this.getElementsByClassName('order-by-content')[0].classList.remove('enabled');
}

for (let item of orderByElements) {
item.addEventListener('click', choseOrder)
};

function choseOrder(){
for (item of orderByElements) {
item.classList.replace('order-disabled', 'order-active')}
this.classList.replace('order-active', 'order-disabled');
order = this.id
loadMovies();
}

for (let item of genresElements) {
item.addEventListener('click', addFilter)
};



for (let item of ratingElements) {
item.addEventListener('click', addFilter)
};

for (let item of criticsElements) {
item.addEventListener('click', addFilter)
};

for (let item of audienceElements) {
item.addEventListener('click', addFilter)
};

function addFilter(){
if (this.classList.contains('order-active')){
this.classList.replace('order-active', 'order-disabled');

}else if(this.classList.contains('order-disabled')){
this.classList.replace('order-disabled', 'order-active')};

thisListName = this.parentNode.parentNode.classList[1];


saveFilter(this.textContent.substring(2), this.classList[1], choseCorrectList(thisListName));
}


function saveFilter(content, itemClass, listName){
if (itemClass == 'order-disabled'){
listName.push(content)}
else if (itemClass == 'order-active'){
listName.splice(genres.indexOf(content), 1);
}
console.log(listName);
}


function choseCorrectList(listName) {
 if (listName == 'genres'){
return genres
}else if (listName == 'rating'){
return rating
}else if (listName == 'critics'){
return critics
}else if (listName == 'audience'){
return audience}}
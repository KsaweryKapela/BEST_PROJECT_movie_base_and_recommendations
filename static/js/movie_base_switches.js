dropdowns = document.getElementsByClassName('order-by');
var dropdownsArray = [].slice.call(dropdowns);
orderByElements = dropdowns[0].getElementsByClassName('order-item');
genresElements = dropdowns[1].getElementsByClassName('order-item');
ratingElements = dropdowns[2].getElementsByClassName('order-item');
criticsElements = dropdowns[3].getElementsByClassName('order-item');
audienceElements = dropdowns[4].getElementsByClassName('order-item');


//making dropdowns work

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

//making all one chose functions work

for (let item of [...orderByElements, ...ratingElements, ...criticsElements, ...audienceElements]) {
item.addEventListener('click', selectItem)
};

function selectItem(){
listOfSiblings = this.parentElement.parentElement.getElementsByClassName('order-item');
dropdownName = this.parentElement.parentElement.classList[1];
if (this.classList.contains('order-disabled') && dropdownName != 'order') {
this.classList.replace('order-disabled', 'order-active')
choseCorrectString(dropdownName, '')
}else{
for (item of listOfSiblings) {
item.classList.replace('order-disabled', 'order-active')}
this.classList.replace('order-active', 'order-disabled');
choseCorrectString(dropdownName, this.id);}
movieIndex = 0;
loadMovies();
}

// making genres work
for (let item of genresElements) {
item.addEventListener('click', addGenreFilter)
};

function addGenreFilter(){
genreName = this.textContent.substring(2)
if (this.classList.contains('order-active')){
this.classList.replace('order-active', 'order-disabled');
genres.push(genreName);
}else{
this.classList.replace('order-disabled', 'order-active')
genres.splice(genres.indexOf(genreName), 1)}
movieIndex = 0;
loadMovies();
}

function choseCorrectString(className, data) {
 if (className == 'order'){
order = data;
}else if (className == 'rating'){
rating = data;
}else if (className == 'critics'){
critics = data;
}else if (className == 'audience'){
audience = data}}
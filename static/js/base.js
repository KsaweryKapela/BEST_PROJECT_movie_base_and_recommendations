const RecommendNavbar = document.getElementsByClassName('nav-item-1')[0];
const MovieBaseNavbar = document.getElementsByClassName('nav-item-2')[0];
const MyMoviesNavbar = document.getElementsByClassName('nav-item-3')[0];


var urls = ['/recommend', '/moviebase', '/']
var allNavbar = document.getElementsByClassName('nav-item');


if (document.URL.split('/')[document.URL.split('/').length - 1] == 'moviebase'){
MovieBaseNavbar.classList.add('item-disabled');}
else if((document.URL.split('/')[document.URL.split('/').length - 1] == 'recommend')){
RecommendNavbar.classList.add('item-disabled');
}
else{MyMoviesNavbar.classList.add('item-disabled');}


for(var i = 0; i < allNavbar.length; i++)
{
  allNavbar[i].addEventListener('click', GoToUrL.bind(i));}


function GoToUrL(){
console.log(this);
window.location.href = urls[this]}

var thrashCan = [].slice.call(document.getElementsByClassName('thrashcan'));
thrashCan.forEach(element => element.addEventListener('click', deleteMovie));



if (document.getElementById('right-arrow-wall')){
const rightArrowWall = document.getElementById('right-arrow-wall')
rightArrowWall.addEventListener('click', clickArrow)}

currentUrl = window.location.href;

const leftArrowWall = document.getElementById('left-arrow-wall')
leftArrowWall.addEventListener('click', clickArrow);


if (currentUrl.charAt(currentUrl.length - 1) == '1'){
leftArrowWall.style.visibility = 'hidden';}

document.getElementsByClassName("button-" + document.URL.split('/')[document.URL.split('/').length - 2])[0].disabled = true;


function clickArrow(){
if (this.id == 'left-arrow-wall'){
newUrl = currentUrl.replace(/.$/, Number(currentUrl.charAt(currentUrl.length - 1)) - 1)
}else if(this.id == 'right-arrow-wall'){
newUrl = currentUrl.replace(/.$/, Number(currentUrl.charAt(currentUrl.length - 1)) + 1)}
window.location.replace(newUrl)}


async function deleteMovie(){
await fetchData('/edit_user_lists', thrashCan.indexOf(this), "rDel", command2=window.location.href);
window.location.replace("/waypoint");
}
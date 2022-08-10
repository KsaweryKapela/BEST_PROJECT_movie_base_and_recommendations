//async function hitsPressed(){
//    movie_index = 0
//    if (hitSwitch.disabled == true){
//    if(hitSwitch.checked){
//        await loadMovies(hits='False');
//
//    }else{
//    await loadMovies(hits='True');}
//    hitSwitch.disabled = false;
//    }else{checkForSwitches()}
//    };
//
//
//async function rottenPressed(){
//    movie_index = 0
//
//    if (rottenSwitch.disabled == true){
//    if(rottenSwitch.checked){
//        await loadMovies(hits=null, rotten='False');
//
//    }else{
//    await loadMovies(hits=null, rotten='True');}
//    rottenSwitch.disabled = false;
//    }else{checkForSwitches()}
//    };
//
//
//async function newPressed(){
//     movie_index = 0
//
//    if (newSwitch.disabled == true){
//    if(newSwitch.checked){
//        await loadMovies(hits=null, rotten=null, liked=null, new_='False');
//
//    }else{
//    await loadMovies(hits=null, rotten=null, liked=null, new_='True');}
//    newSwitch.disabled = false;
//    }else{checkForSwitches()}
//    };
//
//
//async function likedPressed(){
//    movie_index = 0
//
//    if (likedSwitch.disabled == true){
//    if(likedSwitch.checked){
//        await loadMovies(hits=null, rotten=null, liked='False', new_=null);
//
//    }else{
//    await loadMovies(hits=null, rotten=null, liked='True', new_=null);}
//    likedSwitch.disabled = false;
//    }else{checkForSwitches()}
//    };
//
//
//function disableSwitch(dicList){
//dicList[0].style.backgroundColor = "#dce0e6";
//dicList[1].style.backgroundColor = "#c0c6cf";
//dicList[2].style.color = "#8491a3";
//dicList[1].style.cursor = "pointer";
//dicList[1].addEventListener("click", enableSwitch.bind(this, dicList), {once : true})
//dicList[3].disabled = true;
//}
//
//function enableSwitch(dicList){
//dicList[0].style.backgroundColor = "";
//dicList[1].style.backgroundColor = "";
//dicList[2].style.color = "";
//dicList[1].style.cursor = "";
//
//if(dicList[0].id == 'hit-label'){
//hitsPressed();
//
//}else if(dicList[0].id == 'rotten-label'){
//rottenPressed();
//
//}else if(dicList[0].id == 'liked-label'){
//likedPressed();
//
//}else if(dicList[0].id == 'new-label'){
//newPressed();}
//
//disableSwitches();
//};
//
//function disableSwitches(){
//for(index in allSwitches){
//if(allSwitches[index][3].disabled == false){
//disableSwitch(allSwitches[index])};
//}};
//
//
//function checkForSwitches() {
//if (rottenSwitch.disabled == false){
//if(rottenSwitch.checked) {
//loadMovies(hits=null, rotten='False');
//rottenText.textContent = 'ROTTEN';
//}else{
//loadMovies(hits=null, rotten='True');
//rottenText.textContent = 'FRESH'
//}
//
//}else if (hitSwitch.disabled == false){
//if(hitSwitch.checked) {
//loadMovies(hits='False');
//hitText.textContent = 'FLOPS';
//}else{
//loadMovies(hits='True');
//hitText.textContent = 'HITS';
//}}
//
//else if (likedSwitch.disabled == false){
//if(likedSwitch.checked) {
//loadMovies(hits=null, rotten=null, liked='False');
//likedText.textContent = 'HATED';
//}else{
//loadMovies(hits=null, rotten=null, liked='True');
//likedText.textContent = 'LOVED';
//
//}}else if (newSwitch.disabled == false){
//if(newSwitch.checked) {
//loadMovies(hits=null, rotten=null, liked=null, new_='False');
//newText.textContent = 'OLD';
//}else{
//loadMovies(hits=null, rotten=null, liked=null, new_='True');
//newText.textContent = 'NEW';
//
//}}else{
//loadMovies();}}
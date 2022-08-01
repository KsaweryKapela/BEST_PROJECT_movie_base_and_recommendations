const searchSwitch = document.getElementById("search-switch");
const switchLabel = document.getElementById("switch-label");
const searchForm = document.getElementById("search-form");

function pressed(){
    if(switchLabel.textContent=="Films"){
        switchLabel.textContent="Users";
        searchForm.action = "/searchUsers";


    }else {switchLabel.textContent="Films";
    searchForm.action = "/searchFilms";

}}
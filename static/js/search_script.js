searchWrapper = document.getElementById("s-input");
inputBox = document.getElementById("search-input");
suggBox = document.getElementById("sugg-box");
wholeSwitch = document.getElementById("whole-switch");

if (inputBox) {
inputBox.onkeyup = (e)=>{
    wholeSwitch.style.display = 'none';
    let userData = e.target.value;
    let emptyArray = [];

    if(userData){

       if(searchSwitch.checked == false){
       getFetch('/fetch_movies', userData);

       }else{
       getFetch('/fetch_users', userData)};
   }

   else{
        searchWrapper.classList.remove("active");
        wholeSwitch.style.display = 'block';


    }}};


async function getFetch(url, data) {

    const fetch_data = await fetchData(url, data)
    emptyArray = fetch_data['movie_list'];

    for (i = 0; i <= emptyArray.length - 1; i++) {
        emptyArray[i] = '<li id="list-element">'+ emptyArray[i] +'</li>'}

    searchWrapper.classList.add("active");

    let listData;
    if(!emptyArray.length){
        userValue = inputBox.value;
        listData = '<li id="list-element">'+ userValue +'</li>';
    }else{
        listData = emptyArray.join('');
    }
    suggBox.innerHTML = listData;

    let allList = document.getElementById("sugg-box").getElementsByTagName("li");
    for (let i = 0; i < allList.length; i++) {
           allList[i].addEventListener("click", e=> {inputBox.value = (e.target.textContent),
           searchWrapper.classList.remove("active");
           searchForm.submit();

    wholeSwitch.style.display = 'block';
})}};
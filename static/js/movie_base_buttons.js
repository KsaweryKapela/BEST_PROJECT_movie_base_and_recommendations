var icons = [heart, bookmark, dislike, ignore];
var classNames = ['add-movie', 'watch-list', 'dislike', 'ignore'];

iconsN = {
    heart: 'add-movie',
    bookmark: 'watch-list',
    dislike: 'dislike',
    ignore: 'ignore'
}

function lowerIndex() {
    movieIndex -= 4;
    loadMovies()
};

function addIndex() {
    movieIndex += 4;
    loadMovies()
};

function placeArrows() {
    if (movieIndex == 0) {
        leftArrow.style.visibility = "hidden";
    } else {
        leftArrow.style.visibility = "visible"
    }
}

function recognizeIconState(active_icons_list) {


    for (index = 0; index < 4; index++) {

        icons.forEach((icon) => {

            icon[index].addEventListener('click', clickIcon);

            if (icon[index].classList.contains(classNames[icons.indexOf(icon)] + '-enabled')) {
                icon[index].classList.remove(classNames[icons.indexOf(icon)] + '-enabled');
                icon[index].classList.add(classNames[icons.indexOf(icon)] + '-disabled')
            }


            active_icons_list[classNames[icons.indexOf(icon)]].forEach((element) => {

                icon[element].classList.remove(classNames[icons.indexOf(icon)] + '-disabled');
                icon[element].classList.add(classNames[icons.indexOf(icon)] + '-enabled')
            });
        })
    }
}



function clickIcon(iconName) {
    index = defineIndex(this)
    if (this.classList.contains(this.classList[2] + '-disabled')) {

        icons.forEach((element) => {
            value = Object.values(iconsN)[icons.indexOf(element)];
            if (element[index].classList.contains(value + '-enabled'))
                element[index].classList.remove(value + '-enabled')
            element[index].classList.add(value + '-disabled')
        })

        this.classList.remove(this.classList[2] + '-disabled');
        this.classList.add(this.classList[2] + '-enabled');
        fetchData('edit_user_lists', index, command = 'add', this.id)

    } else if (this.classList.contains(this.classList[2] + '-enabled')) {
        this.classList.remove(this.classList[2] + '-enabled');
        this.classList.add(this.classList[2] + '-disabled');
        fetchData('edit_user_lists', index, command = 'del', this.id)
    }
}


function defineIndex(thisIcon) {

    if (thisIcon.id == 'heart') {
        return heart.indexOf(thisIcon)
    } else if (thisIcon.id == 'bookmark') {
        return bookmark.indexOf(thisIcon)
    } else if (thisIcon.id == 'dislike') {
        return dislike.indexOf(thisIcon)
    } else if (thisIcon.id == 'ignore') {
        return ignore.indexOf(thisIcon)
    }
}
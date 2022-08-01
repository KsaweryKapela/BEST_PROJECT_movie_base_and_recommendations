const leftArrow = document.getElementById('left-arrow');
const rightArrow = document.getElementById('right-arrow');

const cardButtons = document.getElementsByClassName('back-icons');

const heart = [document.getElementsByClassName('add-movie')[0], document.getElementsByClassName('add-movie')[1],
               document.getElementsByClassName('add-movie')[2], document.getElementsByClassName('add-movie')[3]];

const bookmark = [document.getElementsByClassName('watch-list')[0], document.getElementsByClassName('watch-list')[1],
               document.getElementsByClassName('watch-list')[2], document.getElementsByClassName('watch-list')[3]];

const dislike = [document.getElementsByClassName('dislike')[0], document.getElementsByClassName('dislike')[1],
               document.getElementsByClassName('dislike')[2], document.getElementsByClassName('dislike')[3]];

const ignore = [document.getElementsByClassName('ignore')[0], document.getElementsByClassName('ignore')[1],
               document.getElementsByClassName('ignore')[2], document.getElementsByClassName('ignore')[3]];


const img = document.getElementsByClassName("movie-base-image");
const img_div = document.getElementsByClassName('filter');

const rottenSwitch = document.getElementById("rotten-switch");
const rottenText = document.getElementById("rotten-text");
const rottenDiv = document.getElementById("rotten-div");
const rottenLabel = document.getElementById("rotten-label");

const hitSwitch = document.getElementById("hit-switch");
const hitText = document.getElementById("hit-text");
const hitDiv = document.getElementById("hit-div");
const hitLabel = document.getElementById("hit-label");

const newSwitch = document.getElementById("new-switch");
const newText = document.getElementById("new-text");
const newDiv = document.getElementById("new-div");
const newLabel = document.getElementById("new-label");

const likedSwitch = document.getElementById("liked-switch");
const likedText = document.getElementById("liked-text");
const likedDiv = document.getElementById("liked-div");
const likedLabel = document.getElementById("liked-label");

var allSwitches = {'rotten':[rottenLabel, rottenDiv, rottenText, rottenSwitch],
                   'hit':[hitLabel, hitDiv, hitText, hitSwitch],
                   'new':[newLabel, newDiv, newText, newSwitch],
                   'liked':[likedLabel, likedDiv, likedText, likedSwitch]};

const freshCheck = document.getElementById('fresh-check');
const dtTitle = document.getElementsByClassName('db-movie-title');
const dtDate = document.getElementsByClassName('db-release-date');
const dtDirector = document.getElementsByClassName('db-director');
const dtTomatometer = document.getElementsByClassName('db-tomatometer');
const dtAudience = document.getElementsByClassName('db-audience');
const dtStudio = document.getElementsByClassName('db-studio');
const dtDescription = document.getElementsByClassName('db-description');
const dtGenres = document.getElementsByClassName('db-genres');
const dtBoxoffice = document.getElementsByClassName('db-boxoffice');
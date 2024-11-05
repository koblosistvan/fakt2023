var currentLesson = 0 //betöltéskor az első óra box van megjelenítve
var sid = ''


function getClassString(group) {
    if (typeof group == 'string') {
        return group;
    } else {
        let out = '';
        for (i=0;i<group.length;i++) {
            out += group[i] + ', ';
        };
        out = out.slice(0, -2); // leszedi a végéről a ', ' részt
        return out;
    }
}

var data; // json
var ts; // timestamp
var cardContainers = [
    [ // cardList-1
        document.querySelector("#cc1-0"), 
        document.querySelector("#cc1-1"), 
        document.querySelector("#cc1-2"), 
        document.querySelector("#cc1-3"),
    ],
    [ // cardList-2
        document.querySelector("#cc2-0"), 
        document.querySelector("#cc2-1"), 
        document.querySelector("#cc2-2"), 
        document.querySelector("#cc2-3"),
    ],
]

// function loadCards() {}
$(document).ready(function() {
    $.ajax({   
        type: "GET",  
        url: "https://tata-refi.hu/nyilt-napp/api/get-lessons.php",
        crossDomain: true,
        dataType: 'json',
        data: "time=0",
        cache:false,
        success: (response)=> {
            console.log("onready ajax sikeres");
            data=JSON.parse(response);
            data = data.lessons;
            ts= new Date(data.update_time); // timestamp
            // ajax hivas utan loadCards()
            loadCards(3,1);
            loadCards(1,2);
        }, 
        error: (response,error)=> {
            console.log("onready ajax sikertelen");
            console.log(error);
            ts = new Date(data_offline.update_time);
            data = data_offline.lessons;
            loadCards(3,1);
            loadCards(1,2);
        },
        complete: ()=>{
            setInterval(()=>{periodicAjaxCall();},3000); // ajax hivas 30 masodpercenkent
        },
    });
});

/*
loadCards() parameterei:
    dayid: melyik napot nezi (0-tol indexelt)
    cardlistid: melyik cardList div-be tegye az orakat
    
    pelda: loadCards(3,1): a harmadik nap (csutortok) napjait tegye be az elso cardlist div-be (#cardList-1)
*/

// ajax hivasok

function periodicAjaxCall() {
    $.ajax({
        type: "GET",
        url: "https://tata-refi.hu/nyilt-napp/api/get-lessons.php",
        crossDomain: true,
        dataType: 'jsonp',
        data: "time=0",
        cache:false,
        success: (response)=>{
            console.log("ajax hivas sikeres");
            data=JSON.parse(response);
            if (new Date(data.update_time) <= ts) {console.log("nem valtozott az adatbazis");return;}
            else {ts = new Date(data.update_time)};
            data = data.lessons;
            // ajax hivas utan loadCardsAjax()
            loadCardsAjax(3,1);
            loadCardsAjax(1,2);
        },
        error: (error)=>{
            console.log("ajax hivas sikertelen");
            console.log(error);
            
            //debugAjaxTest();
        },
    });
};

function debugAjaxTest() {
    data = debug_ajax_test_obj;
    console.log(new Date(data.update_time));console.log(ts);
    if (new Date(data.update_time) <= ts) {console.log("nem valtozott az adatbazis");return;}
    else {ts = new Date(data.update_time);console.log("else ág")};
    data = data.lessons;
    // ajax hivas utan loadCardsAjax()
    loadCardsAjax(3,1);
    loadCardsAjax(1,2);

};


function loadCards(dayid, cardlistid) {

    dayid = dayid.toString();
    //json parse

    let l = data.length;
    //console.log(document.querySelectorAll("#cardList div"))
    //
    //l = 10;
    //
    let cardlist = cardContainers[cardlistid-1];
    var append;
    for (let i=0; i<l; i++) {
        let temp = data[i];
        if (!Boolean(Number(temp.valid))) {continue;};
        if (temp.day != dayid) {continue;};

        let currentId = temp.id.toString();
        let currentPeriod = Number(temp.period);
        if (currentPeriod > 4 || !currentPeriod) {continue;} // elsotol negyedik oraig kell csak (0. sem)

        /* if (valid) { // elso append sorban oda fog tenni egy 'invalid' classt ha invalid
            valid = "";
        } else {
            valid = " invalid";
        } */

        append = '<div class="lesson-card" data-period="' + temp.period + '" '; //data-period attribute a kereséshez kell
        append += 'id="card-' + currentId + '">'; // kell card id

        // ez a három lesz mutatva
        append += '<div class="p-class">' + temp.class + '</div>'; //getClassString(temp.class)
        append += '<div class="p-subject">' + temp.subject + '</div>';
		append += '<div class="p-teacher">' + temp.teacher + '</div>';
        append += '<div class="p-room">' + temp.room + '. terem</div>';

        if (temp.level == "emelt") {
            append += '<div class="emelt">' + temp.level + '</div>';
        } else {
            append += '<div class="alap">' + temp.level + '</div>';
        };

        if (window.location.href.includes("admin")) {
            if (temp.valid == 1) {
                append += '<div class="admin-hide"></div>';
            } else {
                append += '<div class="admin-show"></div>';
            };
        };

        //innentől elrejtve
        //append += '<div class="p-period">' + temp.period + '.</div>';
        append += '<div class="p-time">' + temp.start_time + ' - ' + temp.end_time + '</div>';

        //append += '<p>id: ' + currentId + '</p>';  // id sneak peek

        append += '</div>';
            
        //document.getElementById('cardList').innerHTML += append;
        cardlist[Number(temp.period)-1].innerHTML += append;
    };
};

// ajax hivas utan vegigfut a kartyakon, a timestamp es a valid alapjan kiszedi az elavultakat
function loadCardsAjax() {


    for (let i=0;i<data.length;i++) {
        if (!Boolean(Number(data[i].valid))) {
            let temp = document.getElementById("card-" + data[i].id);
            console.log(temp);
            if (temp) { temp.classList.add("hidden");console.log(data[i].id + ". card eltuntetve"); };
            if (temp) { temp.classList.add("hidden");console.log(data[i].id + ". card eltuntetve"); };
        };
    };
    
};




function filterSubjects() { //tantárgy dropdown select keresés
    var searchSubjectMenu = document.getElementById("subjectSelect");
    var subjectSearchFor = searchSubjectMenu.options[searchSubjectMenu.selectedIndex].value;
    logEvent("subject=" + subjectSearchFor);
    if (subjectSearchFor == document.querySelectorAll("#subjectSelect option")[0].value) { // ha visszamegy az alap opciora
        return;
    };
    var filter;
    var cards = document.getElementsByClassName("lesson-card");
    //console.log(cards)

    for (i=0;i<cards.length;i++) {
        filter = cards[i].outerHTML.toUpperCase();
        if (filter.indexOf(subjectSearchFor.toUpperCase()) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        };
    };

};

// REDUNDÁNS NYILAK SCRIPT
function hideAllLessons() {
    for (i=0;i<4;i++) {
        document.getElementsByClassName("outerCardContainer")[i].classList.add("hidden");
    };
    
};

function lessonSelector(irany) {
    if (currentLesson == 0 && irany == -1) { // ha minimum ala akar menni
        return;
    };
    if (currentLesson == 3 && irany == 1) { // ha maximum fele akar menni
        return;
    };

    // arrow fekete feher formazas
    if ((currentLesson+irany)==3) {
        document.getElementById("next-arrow").classList.add("disabledArrow");
    } else if ((currentLesson+irany)==0) {
        document.getElementById("prev-arrow").classList.add("disabledArrow");
    } else {
        document.getElementById("next-arrow").classList.remove("disabledArrow");
        document.getElementById("prev-arrow").classList.remove("disabledArrow");
    };

    hideAllLessons();
    document.getElementsByClassName("outerCardContainer")[currentLesson + irany].classList.remove("hidden");
    currentLesson += irany;
<<<<<<< HEAD
};
// REDUNDÁNS NYILAK SCRIPT
=======
}
// REDUNDÁNS NYILAK SCRIPT

function showPane(pane) {
    if(pane == 'napValaszto') {
        document.getElementById('napValaszto').classList.remove('hidden');
        document.getElementById('subjectSearch').classList.add('hidden');
        document.getElementById('cardList-1').classList.add('hidden');
        document.getElementById('cardList-1').classList.remove('row');
        document.getElementById('cardList-2').classList.add('hidden');
        document.getElementById('cardList-2').classList.remove('row');
    } else {
        document.getElementById('napValaszto').classList.add('hidden');
        if(pane == 'cardList-1') {

            document.getElementById('aktiv-nap').innerHTML = '11.21';
            logEvent("day=11.21");
        } else {
            document.getElementById('aktiv-nap').innerHTML = '11.26'
            logEvent("day=11.26");
        }
        document.getElementById('subjectSearch').classList.remove('hidden');
        document.getElementById(pane).classList.remove('hidden');
        document.getElementById(pane).classList.add('row');
    }
}

function logEvent(event) {
    $.ajax({   
    type: "POST",  
    url: "https://tata-refi.hu/nyilt-napp/api/log.php",
    crossDomain: true,
    data: "sid=" + sid + "&" + event,
    cache: false
    });
}
>>>>>>> 6e79e307c7741cd8a3b26eaa833125d459d8090f

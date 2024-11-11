/* 3000 -->> 30000 (!!!!!!!!!!!!!!!!!)*/

const DAYS_STRING = [
    "11.21.",
    "11.26.",
]
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
            //console.log(response)
            data=response;//data=JSON.parse(response);
            sid=data.sid;
            ts= data.update_time; // timestamp
            console.log("READY TIMESTAMP: ",ts);

            // ajax hivas utan loadCards()
            data = data.lessons;
            loadCards(3,1);
            loadCards(1,2);
        }, 
        error: (response,error)=> {
            console.log("onready ajax sikertelen");
            console.log(error);
            ts = data_offline.update_time;
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
        dataType: 'json',
        data: "time=0",
        cache:false,
        success: (response)=>{
            console.log("periodikus ajax hivas sikeres");
            data=response;
            if (data.status != "ok") {
                console.log("adatbazis hiba");
            } else {

            if (new Date(data.update_time) <= new Date(ts)) {console.log("nem valtozott az adatbazis");return;}
            else {console.log("valtozott az adatbazis");ts = data.update_time};
            
            data = data.lessons;
            // ajax hivas utan loadCardsAjax()
            console.log("adatok frissitese...");
            loadCardsAjax(3,1);
            loadCardsAjax(1,2);
            };
        },
        error: (error)=>{
            console.log("periodikus ajax hivas sikertelen");
            console.log(error);
        },
    });
};




function loadCards(dayid, cardlistid) {
    dayid = dayid.toString(); //json parse

    let l = data.length;
    let cardlist = cardContainers[cardlistid-1];
    var append;
    for (let i=0; i<l; i++) {
        let temp = data[i];
        if (!Boolean(Number(temp.valid))) {continue;};
        if (temp.day != dayid) {continue;};

        let currentId = temp.id.toString();
        let currentPeriod = Number(temp.period);
        if (currentPeriod > 4 || !currentPeriod) {continue;} // elsotol negyedik oraig kell csak (0. sem)
        
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
function loadCardsAjax(dayid, cardlistid) {
    dayid = dayid.toString();
    let l = data.length;
    var new_text;
    
    for (let i=0; i<l; i++) {
        let temp = data[i];
        if (!Boolean(Number(temp.valid))) {continue;};
        if (temp.day != dayid) {continue;};

        let currentId = temp.id.toString();
        let currentPeriod = Number(temp.period);
        console.log("valtozott id: ",currentId);
        if (currentPeriod > 4 || !currentPeriod) {continue;}

        //new_text = '<div class="lesson-card" data-period="' + temp.period + '" '; //data-period attribute a kereséshez kell
        //new_text += 'id="card-' + currentId + '">'; // kell card id

        new_text = '<div class="p-class">' + temp.class + '</div>'; //getClassString(temp.class)
        new_text += '<div class="p-subject">' + temp.subject + '</div>';
		new_text += '<div class="p-teacher">' + temp.teacher + '</div>';
        new_text += '<div class="p-room">' + temp.room + '. terem</div>';

        if (temp.level == "emelt") {
            new_text += '<div class="emelt">' + temp.level + '</div>';
        } else {
            new_text += '<div class="alap">' + temp.level + '</div>';
        };

        if (window.location.href.includes("admin")) {
            if (temp.valid == 1) {
                new_text += '<div class="admin-hide"></div>';
            } else {
                new_text += '<div class="admin-show"></div>';
            };
        };

        new_text += '<div class="p-time">' + temp.start_time + ' - ' + temp.end_time + '</div>';
        //new_text += '</div>';

        document.getElementById("card-"+currentId).innerHTML = new_text;
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

function logEvent(event) {
    $.ajax({   
    type: "POST",  
    url: "https://tata-refi.hu/nyilt-napp/api/log.php",
    crossDomain: true,
    data: "sid=" + sid + "&" + event,
    cache: false,
    });
    console.log("naplozasi keres elkuldve.");
    console.log("sid: ",sid);
    console.log("log data: ",event);
};

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
            document.getElementById('aktiv-nap').innerHTML = DAYS_STRING[0];
            logEvent("day="+DAYS_STRING[0]);
        } else {
            document.getElementById('aktiv-nap').innerHTML = DAYS_STRING[1];
            logEvent("day="+DAYS_STRING[1]);
        }
        document.getElementById('subjectSearch').classList.remove('hidden');
        document.getElementById(pane).classList.remove('hidden');
        document.getElementById(pane).classList.add('row');
    };
};

// REDUNDÁNS SCRIPT
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
};
// REDUNDÁNS SCRIPT

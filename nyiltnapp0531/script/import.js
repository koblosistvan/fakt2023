/* 3000 -->> 30000 (!!!!!!!!!!!!!!!!!)*/

const DAYS_STRING = [
    "11.11.",
    "11.20.",
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
            data=response;
            sid=data.sid;
            ts= data.update_time;
            data = data.lessons;
            loadCards(1,1);
            loadCards(3,2);
        }, 
        error: (response,error)=> {
            ts = data_offline.update_time;
            data = data_offline.lessons;
            loadCards(3,1);
            loadCards(1,2);
        },
        complete: ()=>{
            setInterval(()=>{periodicAjaxCall();},30000); // ajax hivas 30 masodpercenkent
        }
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
        data: "sid=" + sid + "&time=" + ts,
        cache:false,
        success: (response) => {
            data=response;
            if (data.status == "ok" && data.lessons.length > 0) {
                ts = data.update_time;
                updateCards(data.lessons);
            } ;
        }
    });
};

function createCardHTML(cardData) {
    let cardHTML = '';
    cardHTML += '<div class="p-class">' + cardData.class + '</div>'; 
    cardHTML += '<div class="p-subject">' + cardData.subject + '</div>';
    cardHTML += '<div class="p-teacher">' + cardData.teacher + '</div>';
    cardHTML += '<div class="p-room">' + cardData.room + '. terem</div>';

    if (cardData.level == "emelt") {
        cardHTML += '<div class="emelt">' + cardData.level + '</div>';
    } else {
        cardHTML += '<div class="alap">' + cardData.level + '</div>';
    };

    if (window.location.href.includes("admin")) {
        if (cardData.valid == 1) {
            cardHTML += '<div class="admin-hide"></div>';
        } else {
            cardHTML += '<div class="admin-show"></div>';
        };
    };

    cardHTML += '<div class="p-time">' + cardData.start_time + ' - ' + cardData.end_time + '</div>';

    return cardHTML;
}

function loadCards(dayid, cardlistid) {
    dayid = dayid.toString(); //json parse

    let l = data.length;
    let cardlist = cardContainers[cardlistid-1];
    var append;
    for (let i=0; i<l; i++) {
        let cardData = data[i];
        if (cardData.day != dayid) {continue;};

        let currentId = cardData.id.toString();
        let currentPeriod = Number(cardData.period);
        if (currentPeriod > 4 || !currentPeriod) {continue;} // elsotol negyedik oraig kell csak (0. sem)
        
        let cardClass = 'lesson-card';
        if (cardData.valid == '0') { cardClass += ' hidden';}
        
        let cardHTML = '<div class="' + cardClass + '" data-period="' + cardData.period + '" '; //data-period attribute a kereséshez kell
        cardHTML += 'id="card-' + currentId + '">'; // kell card id
        cardHTML += createCardHTML(cardData);
        cardHTML += '</div>';
            
        cardlist[Number(cardData.period)-1].innerHTML += cardHTML;
    };
};

// ajax hivas utan vegigfut a kartyakon, a timestamp es a valid alapjan kiszedi az elavultakat
function updateCards(lessons) {    
    for (let i=0; i<lessons.length; i++) {
        let cardData = lessons[i];
        let cardDIV = document.getElementById("card-" + cardData.id);

        // láthatóság
        if (cardData.valid == '1' && cardDIV.classList.contains('hidden')) {
            cardDIV.classList.remove('hidden');
        } else if (cardData.valid == '0' && !cardDIV.classList.contains('hidden')) {
            cardDIV.classList.add('hidden');
        };
       
        // tartalom
        document.getElementById("card-"+currentId).innerHTML = createCardHTML(cardData);
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

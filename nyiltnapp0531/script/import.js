var currentLesson = 0 //betöltéskor az első óra box van megjelenítve

function getClassString(group) {
    if (typeof group == 'string') {
        return group;
    } else {
        let out = '';
        for (i=0;i<group.length;i++) {
            out += group[i] + ', '
        }
        out = out.slice(0, -2); // leszedi a végéről a ', ' részt
        return out;
    }
}

function loadCards() {
        let l = data.length;
        //console.log(document.querySelectorAll("#cardList div"))
        //
        //l = 10;
        //
        var cardContainers = [document.querySelector("#cc1"), document.querySelector("#cc2"), document.querySelector("#cc3"), document.querySelector("#cc4")]
        var append;
        for (let i=0; i<l; i++) {
            let temp = data[i];
            let currentId = temp.id.toString();
            let currentPeriod = Number(temp.period)
            
            if (currentPeriod > 4) {continue;} // elso 4 ora kell csak

            append = '<div class="lesson-card" data-period="' + temp.period + '" '; //data-period attribute a kereséshez kell
            append += 'id="card-' + currentId + '">'; // kell card id

            // ez a három lesz mutatva
            append += '<div class="p-class">' + getClassString(temp.class) + '</div>';
            append += '<div class="p-teacher">' + temp.teacher + '</div>';
            append += '<div class="p-room">' + temp.room + '</div>';

            if (temp.level == "emelt") {
                append += '<div class="emelt">' + temp.level + '</div>';
            } else {
                append += '<div class="alap">' + temp.level + '</div>';
            }

            //innentől elrejtve
            append += '<div class="p-period">' + temp.period + '.</div>';
            append += '<div class="p-time">' + temp.starttime + ' - ' + temp.endtime + '</div>';
            append += '<div class="p-subject">' + temp.subject + '</div>';

            //append += '<p>id: ' + currentId + '</p>';  // id sneak peek

            append += '</div>';
            
            //document.getElementById('cardList').innerHTML += append;
            cardContainers[currentPeriod -1 ].innerHTML += append;
        }

}

function filterSubjects() { //tantárgy dropdown select keresés
    var searchSubjectMenu = document.getElementById("subjectSelect")
    var subjectSearchFor = searchSubjectMenu.options[searchSubjectMenu.selectedIndex].value;
    if (subjectSearchFor == document.querySelectorAll("#subjectSelect option")[0].value) { // ha visszamegy az alap opciora
        return;
    }
    var filter;
    var cards = document.getElementsByClassName("lesson-card");
    //console.log(cards)

    for (i=0;i<cards.length;i++) {
        filter = cards[i].outerHTML.toUpperCase();
        if (filter.indexOf(subjectSearchFor.toUpperCase()) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }

}

function hideAllLessons() {
    for (i=0;i<4;i++) {
        document.getElementsByClassName("outerCardContainer")[i].classList.add("hidden");
    }
    
}

function lessonSelector(irany) {
    if (currentLesson == 0 && irany == -1) { // ha minimum ala akar menni
        return;
    }
    if (currentLesson == 3 && irany == 1) { // ha maximum fele akar menni
        return;
    }

    // arrow fekete feher formazas
    if ((currentLesson+irany)==3) {
        document.getElementById("next-arrow").classList.add("disabledArrow")
    } else if ((currentLesson+irany)==0) {
        document.getElementById("prev-arrow").classList.add("disabledArrow")
    } else {
        document.getElementById("next-arrow").classList.remove("disabledArrow")
        document.getElementById("prev-arrow").classList.remove("disabledArrow")
    }

    hideAllLessons();
    document.getElementsByClassName("outerCardContainer")[currentLesson + irany].classList.remove("hidden");
    currentLesson += irany;
}
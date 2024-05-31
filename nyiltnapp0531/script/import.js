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
        console.log(document.querySelectorAll("#cardList div"))
        //
        //l = 10;
        //
        var cardContainers = [document.querySelectorAll("#cc1"), document.querySelectorAll("#cc2"), document.querySelectorAll("#cc3"), document.querySelectorAll("#cc4")]
        var append;
        for (let i=0; i<l; i++) {
            let temp = data[i];
            let currentId = temp.id.toString();
            let currentPeriod = Number(temp.period)
            
            if (currentPeriod > 4) {continue;} // elso 4 ora kell csak

            append = '<div class="card" data-period="' + temp.period + '" '; //data-period attribute a kereséshez kell
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
            append += '<div class="p-period hidden">' + temp.period + '.</div>';
            append += '<div class="p-time hidden">' + temp.starttime + ' - ' + temp.endtime + '</div>';
            append += '<div class="p-subject hidden">' + temp.subject + '</div>';

            //append += '<p>id: ' + currentId + '</p>';  // id sneak peek

            append += '</div>';
            
            //document.getElementById('cardList').innerHTML += append;
            cardContainers[currentPeriod -1 ].innerHTML += append;
        }

}

function filterSubjects() { //tantárgy dropdown select keresés
    var searchSubjectMenu = document.getElementById("subjectSelect")
    var subjectSearchFor = searchSubjectMenu.options[searchSubjectMenu.selectedIndex].value;
    var filter;
    var cards = document.getElementsByClassName("card");
    console.log(cards)

    for (i=0;i<cards.length;i++) {
        filter = cards[i].outerHTML.toUpperCase();
        if (filter.indexOf(subjectSearchFor.toUpperCase()) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

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
        var cardContainers = document.querySelectorAll("#cardList div")
        var append;
        for (let i=0; i<l; i++) {
            let temp = data[i];
            let currentId = temp.id.toString();
            let currentPeriod = Number(temp.period)
            
            if (currentPeriod > 4) {continue;} // elso 4 ora kell csak

            append = '<div class="card" data-period="' + temp.period + '" '; //data-period attribute a kereséshez kell
            append += 'id="card-' + currentId + '">'; // kell card id

            // ez a három lesz mutatva
            append += '<div class="p-time hidden">' + temp.starttime + ' - ' + temp.endtime + '</div>';
            append += '<div class="p-subject">' + temp.subject + '</div>';
            append += '<div class="p-room">' + temp.room + '</div>';

            //append += '<p>id: ' + currentId + '</p>';  // id sneak peek

            //innentől elrejtve
            append += '<div class="p-period hidden">' + temp.period + '.</div>';
            append += '<div class="p-teacher">' + temp.teacher + '</div>';
            append += '<div class="p-class">' + getClassString(temp.class) + '</div>';

            if (temp.level == "emelt") {
                append += '<div class="emelt">' + temp.level + '</div>';
            } else {
                append += '<div class="alap">' + temp.level + '</div>';
            }

            
            append += '</div>';
            
            //document.getElementById('cardList').innerHTML += append;
            cardContainers[currentPeriod -1 ].innerHTML += append;
        }

    }

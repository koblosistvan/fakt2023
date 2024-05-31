function getClassString(group) {
    if (typeof group == 'string') {
        return '<b>osztály: </b>' + group;
    } else {
        let out = '<b>osztályok: </b>';
        for (i=0;i<group.length;i++) {
            out += group[i] + ', '
        }
        out = out.slice(0, -2); // leszedi a végéről a ', ' részt
        return out;
    }
}


function loadCards() {
        let l = data.length;
        //
        //l = 10;
        //
        var cards = document.getElementById('cardList');
        var append;
        for (let i=0; i<l; i++) {
            let temp = data[i];
            let currentId = temp.id.toString();

            append = '<div class="card" data-period="' + temp.period + '" '; //data-period attribute a kereséshez kell
            append += 'id="card-' + currentId + '">'; // kell card id

            // ez a három lesz mutatva
            append += '<p class="p-time"><b>időpont:</b> ' + temp.starttime + ' - ' + temp.endtime + '</p>';
            append += '<p class="p-subject"><b>tantárgy:</b> ' + temp.subject + '</p>';
            append += '<p class="p-room"><b>terem:</b> ' + temp.room + '</p>';

            //append += '<p><b>id:</b> ' + currentId + '</p>';  // id sneak peek

            //innentől elrejtve
            append += '<p class="p-period hidden"><b>óraszám:</b> ' + temp.period + '.</p>';
            append += '<p class="p-teacher hidden"><b>tanár:</b> ' + temp.teacher + '</p>';
            append += '<p class="p-class hidden">' + getClassString(temp.class) + '</p>';

            append += '></label >';
            append += '</div>';
            cards.innerHTML += append;
        }

    }

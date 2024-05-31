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
        //
        //l = 10;
        //
        var cards = document.getElementById('cardList');
        var append;
        for (let i=0; i<l; i++) {
            let temp = data[i];
            let currentId = temp.id.toString();

            append = '<span class="card" data-period="' + temp.period + '" '; //data-period attribute a kereséshez kell
            append += 'id="card-' + currentId + '">'; // kell card id

            // ez a három lesz mutatva
            append += '<span class="p-time hidden">' + temp.starttime + ' - ' + temp.endtime + '</span>';
            append += '<span class="p-subject">' + temp.subject + '</span>';
            append += '<span class="p-room">' + temp.room + '</span>';

            //append += '<p><b>id:</b> ' + currentId + '</p>';  // id sneak peek

            //innentől elrejtve
            append += '<span class="p-period hidden">' + temp.period + '.</span>';
            append += '<span class="p-teacher">' + temp.teacher + '</span>';
            append += '<span class="p-class">' + getClassString(temp.class) + '</span>';
            append += '<span class="p-class">' + temp.level + '</span>';

            
            append += '</span>';
            cards.innerHTML += append;
        }

    }

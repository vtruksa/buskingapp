$(window).on('message', function(event) {
    
    slots = event.originalEvent.data.data
    console.log(slots)
    html = ""
    slots.forEach(e => {
        radio = '<input name="book_show" class="form-radio" type="radio" value="'+ e.id +'" id="book'+ e.id +'">'
        if(e.artist != -1) {radio = 'booked'}
        console.log(e.artist)
        html += `
            <tr>
            <td>`+radio+`</td>
                <td>`+e.spot+`</td>
                <td>`+ e.date +`</td>
                <td>`+e.time.start + ' - '+e.time.end+`</td>
            </tr>
        `
    });

    html += `<tr><td colspan='3' class="btn-cell"><button class="btn btn-primary" id="book-btn">Zarezervovat</button></td></tr>`

    $('#timetable table tbody').html(html)
})    
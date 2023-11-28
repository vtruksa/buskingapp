spot_id = -1

$(document).ready(function() {
    console.log('ready')

    $(window).on('message', function(event) {
        if(event.originalEvent.data.t == 'click') {
            coordinates = event.originalEvent.data.coordinates;
            $('#coordinates').val(''+coordinates)
        } else if(event.originalEvent.data.t == 'load') {
            data = event.originalEvent.data.data
            $('#spot_id').val(data.id)
            $('#coordinates').val(data.lan + ', ' + data.lon)
            $('#name').val(data.name)
            $('#description').val(data.description)
            allowedSlots = data.allowedSlots.split(';')
            $('.times').each(function() {
                input = $(this).find('input')[0]
                if(allowedSlots.includes(input.id)) {
                    input.setAttribute('checked', 'checked')
                } else {
                    input.removeAttribute('checked')
                }
            })
        }
    })
})

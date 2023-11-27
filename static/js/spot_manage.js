$(document).ready(function() {
    console.log('ready')

    $(window).on('message', function(event) {
        coordinates = event.originalEvent.data.coordinates;
        $('#coordinates').val(''+coordinates)
    })
})

function loadShows(btn) {
    console.log(btn.id)
    $.ajax({
        url:'/api/load-shows/',
        method:'GET',
        data:{'id':btn.id, 'times':null},
        success: function(data) {
            window.parent.postMessage({'t':'load',data})
        },
        error: function(data) {
            console.log(data)
        }
    })
}
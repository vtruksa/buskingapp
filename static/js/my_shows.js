$(document).ready(function() {
    $('.delbooking').on('click', function() {del_booking(this)})
    console.log('ready')
})

function del_booking(btn) {
    id = btn.id.replace('del', '')
    
}
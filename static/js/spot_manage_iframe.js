lonlan = [0, 0]


$(document).ready(function() {
    $(document).click(function() {
        pasteClip()
    })
}) 

function editSpot(button) {
    id = button.id.replace('edit', '')
    
    $.ajax({
        url:'/api/get-spot/',
        method:'GET',
        data: {'id':id},
        success: function(data) {
            window.parent.postMessage({'t':'load',data})
        },
        error: function(data) {
            console.log(data)
        }
    })
}

function deleteSpot(button) {
    id = button.id.replace('delete', '')

    $.ajax({
        url:'/api/del-spot/',
        method:'GET',
        data: {'id':id},
        success: function() {window.top.location.reload()},
        error: function(data) {console.log(data)}
    })
}

async function pasteClip() {
    try {
        navigator.clipboard.readText().then((coordinates) => {
            try {
                c = coordinates.split(',')
                if(c.length == 2) {
                    coordinates = c
                
                    window.parent.postMessage({'t':'click', 'coordinates':coordinates})
                }
            }
            catch {}
        })
    }
    catch {
        console.error('there was an error getting coordinates you clicked')
    }
}
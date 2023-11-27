$(document).ready(function() {
    $(document).click(function() {
        pasteClip()
    })
}) 

async function pasteClip() {
    try {
        navigator.clipboard.readText().then((coordinates) => {
            console.log('coordinates: ' + coordinates)
            window.parent.postMessage({'coordinates':coordinates})
        })
    }
    catch {
        console.error('there was an error getting coordinates you clicked')
    }
}
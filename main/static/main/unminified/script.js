document.querySelector('.pill').addEventListener('click',(ev)=>{
    document.querySelector('.vert-container').classList.toggle('open')
})

var overlay = document.querySelector('#loader');

window.addEventListener('load', (ev)=>{
    if(document.querySelectorAll('#yourevents .event-div').length===0){
        console.log("No events")
        document.querySelector('#yourevents img#errorsvg').style.display = "block"
    }
})
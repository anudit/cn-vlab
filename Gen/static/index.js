
function updateImage(){
    let bin = document.getElementById('binInput').value;
    document.getElementById('submitBtn').innerHTML = `<i class="material-icons left">hourglass_full</i>Loading`;
    fetch(`./image/${bin}`)
    .then(response => response.json())
    .then((data) =>{
        document.getElementById('encImage').src = data['url'];
        document.getElementById('submitBtn').innerHTML = `<i class="material-icons left">check</i>Submit`;
    })
    .catch((error)=>{
        console.log(error);
        document.getElementById('submitBtn').innerHTML = `<i class="material-icons left">check</i>Submit`;
    });

}

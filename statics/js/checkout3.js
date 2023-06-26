document.addEventListener('DOMContentLoaded', function(){
    const scanner= new Html5QrcodeScanner(
        'reader',{
        qrbox:{
            width:250,
            height:250,
        },
        fps:20,
    });
    scanner.render(success);
});

function success(result) {
    /*change value*/
    var input=document.getElementById("result");
    input.value=result;

    /*change reader to success message*/
    document.getElementById('reader').innerHTML = ``;
    document.getElementById('choose').innerHTML = `<h4>Scan Result</h4>`;

    scanner.clear();
}
function error(err){
    console.error(err);
}


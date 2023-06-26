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
    /*change reader to success message*/
    document.getElementById('reader').innerHTML = ``;
    document.getElementById('choose').innerHTML = ``;
    
    /*change value*/
    var input=document.getElementById("result");
    input.value=result;

    // document.getElementById('reader').innerHTML = `
    // <h2>Success!</h2>
    // <p><a href="${result}">${result}</a></p>
    // `;

    scanner.clear();
}
function error(err){
    console.error(err);
}


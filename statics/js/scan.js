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

    document.getElementById('scanned_data').innerHTML=result;
    // document.getElementById('result').innerHTML = `
    // <h2>Success!</h2>
    // <p><a href="${result}">${result}</a></p>
    // `;

    // scanner.clear();

    document.getElementById('reader').remove();
    // document.getElementById('scanned_data').value=result;
}
// function error(err){
//     console.error(err);
// }

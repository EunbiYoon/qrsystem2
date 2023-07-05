function copyText(element){
    var textToCopy=element.textContent.slice(0,-1);
    navigator.clipboard.writeText(textToCopy).then(function(){
        element.textContent='Copied!';
        setTimeout(function(){
            element.innerHTML=textToCopy+' <button><i class="fa fa-copy"></i></button>';
        }, 2000);
    })
    .catch(function (error){
        console.error('Unable to copy text: ',error)
    });
}
function copyText(element){
    var textToCopy=element.textContent;
    navigator.clipboard.writeText(textToCopy).catch(function(error){
        console.error("Unable to copy", error)
    });
}

    document.addEventListener('DOMContentLoaded',function(){
        fetch('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example').then(response => response.blob()).then(blob => {
            console.log(document.querySelector('.field-old_url'))
        })
    })
    
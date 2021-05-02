function previewFile() {
    let preview = document.querySelector('img');
    let file    = document.querySelector('input[type=file]').files[0];
    let reader  = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
    }
}

// ************************

// The scroll-down function
// document.getElementsByClassName("btn-main").addEventListener('click', function() {
//     //   let scrollDistance = document.documentElement.clientHeight;   
//     //   window.scrollBy(0, scrollDistance);
//     let pageHeight = window.innerHeight;
//     window.scrollBy(0, pageHeight);
//     });

function goDown() {
       let pageHeight = window.innerHeight + 50;
        window.scrollBy(0, pageHeight);
}

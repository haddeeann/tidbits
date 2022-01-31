let itemsCount = document.getElementsByClassName("number-items boss-number-items nonzero-items")[0].innerHTML;

let money = document.getElementsByClassName('subtotal')[0].innerHTML;

let imgArr = [];
document.getElementById('tr_phase2_ShoppingBg').click();
setTimeout(() => {
    let images = document.getElementsByClassName('kas-newpb-product-image');

    for(let i = 0; i < images.length; i++) {
        //console.log(images[0]);
        imgArr.push(images[0].src);
    }
}, 1000);

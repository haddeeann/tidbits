function loop(el) {
    if(el.children.length > 0) {
        for(let i of el.children) {
            loop(i);
        }
    } else {
        el.textContent = el.textContent.replace(/cook/g, "ruin");
        el.textContent = el.textContent.replace(/Cook/g, "Ruin");
    }
}
let r = document.getElementsByClassName('recipe-instructions')[0];

loop(r);

// for(let i of wonder.children) {
//     console.log(i);
// }

// console.log(wonder.children);

// console.log(wonder.hasChildNodes());

// console.log(wonder.childNodes);

let pathname = window.location.pathname;
let category = '';
if(pathname.search('product-category') === 1) {
    let index = pathname.indexOf('/', 1);
    index++;
    category = pathname.slice(index, pathname.length - 1);
}

window.addEventListener('submit', (event) => {
    event.preventDefault();
});

let loginEmail = '';
let regEmail = '';
let updateEmail = '';

let login = document.getElementById('username');
login.addEventListener('change', (event) => {
    loginEmail = login.value;
    console.log(loginEmail);
});

let reg = document.getElementById('reg_email');
reg.addEventListener('change', (event) => {
    regEmail = reg.value;
    console.log(regEmail);
});

let update = document.getElementById('input_1_1');
update.addEventListener('change', (event) => {
    updateEmail = update.value;
    console.log(updateEmail);
});







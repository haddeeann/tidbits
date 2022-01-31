if(product) {
    let pathname = window.location.pathname;
    let startIndex = pathname.indexOf('/', 1);
    startIndex++;
    let categoryProduct = pathname.slice(startIndex, pathname.length - 1);
    document.cookie = `categoryProduct = ${categoryProduct}`;
}
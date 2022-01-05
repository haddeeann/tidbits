var isPalindrome = function(x) {
    const str = x.toString();
    const mid = Math.floor(str.length/2);
    const end = str[str.length - 1];
    for(let i = 0; i <= mid; i++) {
        if(str[i] !== str[end - i]) {
            return false;
        }
    }

    return true;
};

const str = isPalindrome(-131);
console.log(str);
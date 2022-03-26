var isPalindrome = function(x) {
    const str = x.toString();
    const mid = Math.floor(str.length/2);
    const end = str.length - 1;
    for(let i = 0; i <= mid; i++) {
        if(str[i] !== str[end - i]) {
            return false;
        }
    }

    return true;
};
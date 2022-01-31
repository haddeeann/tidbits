var reverse = function(x) {
    let reversed = String(Math.abs(x)).split('').reverse().join('');
    if(parseInt(reversed) > Math.pow(2, 31) - 1) {
        return 0;
    }

    return x < 0 ? -reversed : reversed;
};
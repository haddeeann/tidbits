var myAtoi = function(s) {
    const st = s.trim();
    if(st[1] === '+' || st[1] === '-' || st[1] === ' ') {
        return 0;
    }
    let sign = st[0] === '+' || st[0] == '-' ? st[0] : null;
    let num = sign ? parseInt(st.slice(1)) : parseInt(st);
    if(Number.isNaN(num)) {
        return 0;
    }
    if(sign && sign === '-' && num >= Math.pow(2, 31)) {
        return -Math.pow(2, 31);
    } else if(!sign || sign !== '-') {
        if(num >= Math.pow(2, 31) - 1) {
            return Math.pow(2, 31) - 1;
        }
    }

    return sign === '-' ? parseInt(sign + num) : num;
};
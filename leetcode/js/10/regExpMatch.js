var isMatch = function(s, p) {
    let ex = `^${p}$`;
    let reg = new RegExp(ex);
    return reg.test(s);
};
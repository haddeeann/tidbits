var intToRoman = function(num, r = '') {
    const M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1;
    const IV = 4, IX = 9;
    const XL = 40, XC = 90;
    const CD = 400, CM = 900;
    if(num === 0) {
        return r;
    }
    switch(true) {
        case num >= CM:
            r += num >= M ? 'M' : 'CM';
            num -= num >= M ? M : CM;
            break;
        case num >= CD:
            r += num >= D ? 'D' : 'CD';
            num -= num >= D ? D : CD;
            break;
        case num >= XC:
            r += num >= C ? 'C' : 'XC';
            num -= num >= C ? C : XC;
            break;
        case num >= XL:
            r += num >= L ? 'L' : 'XL';
            num -= num >= L ? L : XL;
            break;
        case num >= IX:
            r += num >= X ? 'X' : 'IX';
            num -= num >= X ? X : IX;
            break;
        case num >= IV:
            r += num >= V ? 'V' : 'IV';
            num -= num >= V ? V : IV;
            break;
        case num >= I:
            r += 'I';
            num -= I;
            break;
        default:
            console.log(`you got yourself a negative number there pal. or maybe a zero`);
            break;
    }

    if(num >= 0) {
        return intToRoman(num, r);
    }
};

console.log(intToRoman(1994));
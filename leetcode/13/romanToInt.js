var romanToInt = function(s) {
    let str = s.split('');
let i = s.length - 1;
let sum = 0;
let obj = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}
while(str.length > 0) {
    let combo = str.length > 1 ? str[i-1] + str[i] : null;
    let letter = str[i];
    if(combo && obj[combo]) {
        sum += obj[combo];
        str.splice(i-1);
        i -= 2;
        continue;
    }
    sum += obj[letter];
    str.pop();
    i--;
}

return sum;
};
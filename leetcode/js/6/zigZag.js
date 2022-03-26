var convert = function(s, numRows) {
    if(s.length < numRows || s.length < 3 || numRows === 1) {
        return s;
    }

    let result = [];
    let string = s.split('');
    let col = 0;
    for(let i = 0; i < numRows; i++) {
        result.push([]);
    }

    result[0][0] = string.shift();

    while(string.length > 0) {
        for(let j = 1; j < numRows; j++) {
            result[j][col] = string.shift();
        }
    
        for(let k = numRows - 2; k >= 0; k--) {
            col++;
            result[k][col] = string.shift();
        }
    }

    return result.flat().join('');
};
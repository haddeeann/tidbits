var letterCombinations = function(digits) {
    if(digits === '' || digits.length === 0) {
        return [];
    }
    let digitArr = [];
    const letterD = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    for(let i of digits) {
        digitArr.push(letterD[i]);
    }

    return loopThruArr(digitArr, digits.length);
};

function loopThruArr(entryArray, digitsLength) {
    let entryArrayCopy = [];
    let startRow = entryArray.shift();
    let resultArr = [];
    let answerArr = [];
    if(entryArray.length === 0) {
        return startRow;
    }

    for(let startVal of startRow) {
        entryArrayCopy = entryArray.slice();
        resultArr = searchAdd(entryArrayCopy, startVal, digitsLength);
        answerArr = [...answerArr, ...resultArr];
    }

    return answerArr;
}

function searchAdd(damnArray, start, digitsLength) {
    let addArr = [];
    let resultsArr = [];
    while(damnArray.length > 0) {
        let nextRow = damnArray.shift();
        if(addArr.length === 0) {
            for(let i = 0; i < nextRow.length; i++) {
                addArr.push(start + nextRow[i]);
            }
            continue;
        }

        let baseLetters = nextRow.slice(); // copy of next row so row isn't affected
        let addRowArr = addArr.slice(); // get copy of the current contents of the add array 
        while(baseLetters.length > 0) {
            let nextLetter = baseLetters.shift();
            for(let letters of addRowArr) {
                let combo = letters + nextLetter;
                addArr.push(combo);
                if(combo.length === digitsLength) {
                    resultsArr.push(combo);
                }
            }
        }
    }

    return resultsArr.length > 0 ? resultsArr : addArr;
}
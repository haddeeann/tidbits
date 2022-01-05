function loopThruArr(entryArray) {
    let entryArrayCopy = [];
    let startRow = entryArray.shift();
    let resultArr = [];
    let answerArr = [];

    for(let startVal of startRow) {
        entryArrayCopy = entryArray.slice();
        resultArr = searchAdd(entryArrayCopy, startVal);
        answerArr = [...answerArr, ...resultArr];
    }

    console.log(answerArr);
}

function searchAdd(damnArray, start) {
    let addArr = [];

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
                addLetters(letters, nextLetter);
            }
        }
    }

    function addLetters(addLetters, letter) {
        let combo = addLetters + letter;
        addArr.push(combo);
    }

    return addArr;
}

loopThruArr([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]);
function loopThruArr(damnArray) {
    const addArr = searchAdd(damnArray);

    console.log(addArr);
}

function searchAdd(damnArray) {
    let start = 'a';
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

loopThruArr([['at', 'b', 'c'], ['d', 'e', 'f']]);
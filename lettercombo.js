/**
 * @param {string} digits
 * @return {string[]}
 */
function play () {
    let nodeArr = [];
    let arr = ['d', 'e', 'f'];
    let arr2 = ['g', 'h', 'i'];

    addStrArr(arr, arr2);
    // console.log(nodeArr);
}

// add two rows and put results in a results array
function addStrArr(rowArr, rowArr2) {
    let adderArr = [];
    let letter = 'a';

    rowAdder(rowArr, letter);

    let adderArrSlice = adderArr.slice();

    while(adderArrSlice.length > 0) {
        let newLetterCombo = adderArrSlice.shift();
        console.log(newLetterCombo);
        let rowArr = rowArr2.slice();
        rowAdder(rowArr, newLetterCombo);
    }

    function rowAdder (rowArr, prevLetter) {
        while(rowArr.length > 0) {
            let nextLetter = rowArr.shift();
            adder(prevLetter, nextLetter);
        }
    }

    function adder (letter1, letter2) {
        let letterCombo = letter1 + letter2;
        adderArr.push(letterCombo);
    }

    console.log(adderArr);
    // return adderArr;
}

play();
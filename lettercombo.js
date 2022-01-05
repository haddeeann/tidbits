/**
 * @param {string} digits
 * @return {string[]}
 */
function play () {
    let nodeArr = [];
    let letterArr = ['a', 'b', 'c'];
    let arr = ['d', 'e', 'f'];
    let arr2 = ['g', 'h', 'i'];
    let arr3 = ['j', 'k', 'l'];

    addStrArr(letterArr, arr, arr2, arr3);
    // console.log(nodeArr);
}

// add two rows and put results in a results array
function addStrArr(letterArr, rowArr1, rowArr2, rowArr3) {
    let addingThatDamnArray = [rowArr2, rowArr3];
    let adderArr = [];
    let letterBase = letterArr[0];

    // pattern building
    // step one
    rowAdder(rowArr1, letterBase);

    while(addingThatDamnArray.length > 0) {
        let rowArray = addingThatDamnArray.shift();
        console.log(rowArray);
        let arrSlice = adderArr.slice();

        while(arrSlice.length > 0) {
            let letterBase = arrSlice.shift();
            // call to the row adder
            let rowArrSlice = rowArray.slice();
            rowAdder(rowArrSlice, letterBase);
        }
    }

    // step two
    // let arrSlice = adderArr.slice();

    // while(arrSlice.length > 0) {
    //     let letterBase = arrSlice.shift();
    //     // call to the row adder
    //     let rowArrSlice = rowArr2.slice();
    //     rowAdder(rowArrSlice, letterBase);
    // }

    // arrSlice = adderArr.slice();

    // while(arrSlice.length > 0) {
    //     let letterBase = arrSlice.shift();
    //     // call to the row adder
    //     let rowArrSlice = rowArr3.slice();
    //     rowAdder(rowArrSlice, letterBase);
    // }

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
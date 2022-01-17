var fourSum = function(nums, target) {
    let sorted = mergeSort(nums);
    console.log(sorted);
    // pivot points
    let mid = Math.floor(sorted.length/2); // midpoint
    let first = Math.floor(mid/2); // first quarter
    let end = sorted.length - 1; // end point
    let second = Math.floor(((end - mid) / 2) + mid);
    console.log(sorted[0]);
    console.log(sorted[first]);
    console.log(sorted[mid]);
    console.log(sorted[second]);
    console.log(sorted[end]);
    // for(let i = 0; i <= pivot; i++) {
    //     console.log(`start ${sorted[i]}`);
    //     console.log(`first ${sorted[first]}`);
    //     console.log(`middle ${sorted[pivot]}`);
    //     console.log(`end ${sorted[end - i]}`);
    //     console.log('--------');
    // }
};

function mergeSort(arr) {
    if(arr.length === 1) {
        return arr;
    }

    let mid = Math.floor(arr.length / 2);
    let left = arr.slice(0, mid);
    let right = arr.slice(mid);

    return sort(mergeSort(left), mergeSort(right));
}

function sort(left, right) {
    let result = [];

    while(left.length > 0 && right.length > 0) {
        if(left[0] < right[0]) {
            result.push(left.shift());
        } else {
            result.push(right.shift());
        }
    }

    return [...result, ...left, ...right];
}

//fourSum([1,0,-1,0,-2,2], 0);
fourSum([1,10,-3,6,-2,2,4,4,3,-5], 0);
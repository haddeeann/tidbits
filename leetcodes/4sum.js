var fourSum = function(nums, target) {
    let sorted = mergeSort(nums);
    let start = null;
    let q1 = null;
    let mid = null;
    let q2 = null;
    let end = null;

    while(sorted.length > 0) {
        // pivot points
        start = 0;
        mid = Math.floor(sorted.length/2); // midpoint
        q1 = Math.floor(mid/2); // first quarter
        q2 = Math.floor(q1 + mid); // q2
        end = sorted.length - 1; // end point
        console.log(`${sorted[start]} + ${sorted[q1]} + ${sorted[mid]} + ${sorted[q2]} + ${sorted[end]}`)
        sum = sorted[start] + sorted[q1] + sorted[mid] + sorted[q2] + sorted[end];
        console.log(`sum is ${sum}`);
        sorted.shift();
    }
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
fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0);
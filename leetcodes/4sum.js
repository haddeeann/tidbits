var fourSum = function(nums, target) {
    // let sum = null;
    console.log(nums);

    for(let r = 3; r < nums.length; r++) {
        let u = 0;
        let t = 1;
        let s = 2;
        while(r - s > 1) {
            s++;
            while(s - t > 1) {
                t++;
                while(t - u > 1) {
                    u++;
                }
            }
        }
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
fourSum([-4, -3, -2, -1, 0, 0, 1, 2, 3, 4], 0);


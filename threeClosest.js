var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => {
        return a - b;
    });
    let sum = null;
    let diff = null;
    let leastDiff = null;
    let ldSum = null; // the sum when the leastDiff is obtained

    for(let i = 0; i < nums.length - 2; i++) {
        let high = nums.length - 1;
        let low = i + 1;
        while(low < high) {
            sum = nums[low] + nums[high] + nums[i];
            diff = Math.abs(target - sum);

            if(!leastDiff || diff < leastDiff) {
                ldSum = sum;
                leastDiff = diff;
            } 

            while (nums[low] === nums[low+1]) low++;
            while (nums[high] === nums[high-1]) high--;

            if(sum > target) {
                high--;
            } else if(sum < target) {
                low++;
            } else {
                return sum;
            }
        }
    }

    return ldSum;
};

threeSumClosest([0,0,0], 1);
var threeSum = function(nums) {
    let answer = [];
    nums.sort((a, b) => {
        return a - b;
    });

    for(let i = 0; i < nums.length - 2; i++) {
        if(i === 0 || nums[i] !== nums[i - 1]) {
            let low = i + 1;
            let high = nums.length - 1;
            let sum = -nums[i];
            while(low < high) {
                if(nums[low] + nums[high] === sum) {
                    answer.push([nums[i], nums[low], nums[high]]);
                    while (low < high && nums[low] === nums[low + 1]) low++;
                    while (low < high && nums[high] === nums[high - 1]) high--;
                    low++;
                    high--;
                } else if (nums[low] + nums[high] > sum) {
                    high--;
                } else {
                    low++;
                }
            }
        }
    }
    console.log(answer);
    return answer;
};
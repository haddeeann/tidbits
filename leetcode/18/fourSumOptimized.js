var fourSum = function(nums, target) {
    nums.sort((a, b) => {
        return a - b;
    });
    let obj = {};
    for(let i = 0; i < nums.length; i++) {
        for(let j = i + 1; j < nums.length; j++) {
            let left = j + 1;
            let right = nums.length - 1;
            while(left < right) {
                let tmpArr = [nums[i], nums[j], nums[left], nums[right]];
                let sum = nums[i] + nums[j] + nums[left] + nums[right];
                if(!obj[tmpArr] && sum === target) {
                    obj[tmpArr] = undefined;
                }
                if(sum > target) {
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
    }
    
    let ansKeys = [];
    let keyObj = Object.keys(obj);
    keyObj.forEach((k) => {
        ansKeys.push(k.split(','));
    });
    return ansKeys;
};
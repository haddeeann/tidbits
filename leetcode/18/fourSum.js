var fourSum = function(nums, target) {
    nums.sort((a, b) => {
        return a - b;
    });
    let obj = {};
    for(let i = 0; i < nums.length; i++) {
        for(let j = i + 1; j < nums.length; j++) {
            for(let k = j + 1; k < nums.length; k++) {
                for(let l = k + 1; l < nums.length; l++) {
                    let tmpArr = [nums[i], nums[j], nums[k], nums[l]];
                    if(!obj[tmpArr] && nums[i] + nums[j] + nums[k] + nums[l] === target) {
                        obj[tmpArr] = undefined;
                    }
                }
            }
        }
    }
    
    let ansKeys = [];
    let keyObj = Object.keys(obj);
    keyObj.forEach((k) => {
        ansKeys.push(k.split(','));
    });
    console.log(ansKeys);
};

fourSum([-2, -1, 0, 0, 1, 1, 1, 2, 2], 0);
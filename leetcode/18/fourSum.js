var fourSum = function(nums, target) {
    nums.sort((a, b) => {
        return a - b;
    });

    let obj = {};
    for(let i = 0; i < nums.length; i++) {
        if(i !== 0 && nums[i] === nums[i - 1]) {
            continue;
        }
        for(let j = i + 1; j < nums.length; j++) {
            if(j !== 1 && nums[j] === nums[j -1]) {
                continue;
            }
            for(let k = j + 1; k < nums.length; k++) {
                if(k !== 2 && nums[k] === nums[k - 1]) {
                    continue;
                }
                for(let l = k + 1; l < nums.length; l++) {
                    if(l !== 3 && nums[l] === nums[l - 1]) {
                        continue;
                    }
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
    return ansKeys;
};

console.log(fourSum([ -2, -1, 0, 0, 1, 2 ], 0));
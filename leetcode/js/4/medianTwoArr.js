var findMedianSortedArrays = function(nums1, nums2) {
    if(nums1.length === 0 && nums2.length === 0) {
        return 0;
    }
    let arrLength = nums1.length + nums2.length;
    let answer = [];
    let midpoint = arrLength % 2 === 0 ? Math.floor(arrLength/2) - 1 : Math.floor(arrLength/2);

    let index = 0;
    while(nums1.length > 0 || nums2.length > 0) {
        if(nums1.length > 0 && nums2.length > 0) {
            nums1[0] < nums2[0] ? answer.push(nums1.shift()) : answer.push(nums2.shift());
        } else if(nums1.length > 0) {
            answer = [...answer, ...nums1];
            break;
        } else if(nums2.length > 0) {
            answer = [...answer, ...nums2];
            break;
        }
        if(index === midpoint + 1) {
            break;
        }
        index++;
    }
    if(arrLength % 2 === 0) {
        return (answer[midpoint] + answer[midpoint + 1])/2;
    } else {
        return answer[midpoint];
    }
};
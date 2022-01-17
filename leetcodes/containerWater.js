var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let area = 0;
    let maxArea = 0;
    while(left < right) {
        if(height[left] <= height[right]) {
            area = height[left] * (right - left);
            maxArea = Math.max(area, maxArea);
            left++;
        } else if(height[right] <= height[left]) {
            area = height[right] * (right - left);
            maxArea = Math.max(area, maxArea);
            right--;
        }
    }

    return maxArea;
};

maxArea([1,8,6,2,5,4,8,3,7]);
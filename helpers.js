function frankenSplice(arr1, arr2, n) {
    let arr = arr2.slice(0, n).concat(arr1).concat(arr2.slice(n));
    console.log(arr);
  }
  
  frankenSplice([1, 2, 3], [4, 5, 6], 1);
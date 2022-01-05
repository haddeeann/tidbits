const sum = (num1, num2, callback) => {
    setTimeout(() => {
        callback(num1 + num2);
    }, 2000);
}

sum(1, 4, (sum) => {
    console.log(sum);
});
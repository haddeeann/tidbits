var longestPalindrome = function(s) {
    let longest = 0; // longest num value
    let lText = ''; // longest word
    let test = '';
    let test2 = '';
    let testLength = 0;
    for(let i = 0; i < s.length; i++) {

        test = s.slice(i);
        if(test.length > longest) {
            testLength = testPal(test);
            if(testLength > longest) {
                longest = testLength;
                lText = test;
                console.log(lText);
            }
            for(let j = test.length; j > 0; j--) {
                test2 = test.slice(0, j);
                if(test2.length > longest) {
                    testLength = testPal(test2);
                    if(testLength > longest) {
                        longest = testLength;
                        lText = test2;
                        console.log(lText);
                    }
                }
            }
        } else {
            continue;
        }
    }
    console.log(lText);
    return lText;
};

function testPal(s) {
    let mid = Math.floor(s.length/2);
    let split1 = s.slice(0, mid);
    let split2 = s.length % 2 === 0 ? s.slice(mid) : s.slice(mid + 1);
    if(split1.localeCompare(split2) === 0) {
        return s.length;
    }

    return 0;
}

console.log(longestPalindrome('babad'));
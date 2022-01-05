function longestPalindrome(s) {
    let indexArr = [];
    let sliced = '';
    let testStr = '';
    let pal = '';
    let strObj = {};
    let longest = 1;
    let longestStr = s[0];
    for(let i = 0; i < s.length; i++) {
        sliced = s.slice(i);
        // if there is another letter
        if(sliced.indexOf(sliced[0], 1) !== -1 && sliced.length > longest) {
            indexArr = findIndex(sliced);
            for(let j = indexArr.length - 1; j >= 0 ; j--) {
                testStr = sliced.slice(0, indexArr[j] + 1);
                testStrLength = testStr.length;
                if(!strObj[testStr] && testStr.length > longest) {
                    strObj[testStr] = testStr.length;
                    pal = testPalindrome(testStr);
                    if(pal.length > 0 && pal.length > longest) {
                        longest = pal.length;
                        longestStr = pal;
                    }
                }
            }
        }
    }

    return longestStr;
}

function testPalindrome(s) {
    const mid = Math.floor(s.length/2);
    for(let i = 0; i < mid; i++) {
        if(s[i] !== s[s.length - 1 - i]) {
            return '';
        }
    }

    return s;
}

function findIndex(s) {
    let i = 0;
    let arr = [];
    while((i = s.indexOf(s[0], i + 1)) >= 0) {
        arr.push(i);
    }
    return arr;
}
//longestPalindrome('abcdcba')
longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
//longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth');
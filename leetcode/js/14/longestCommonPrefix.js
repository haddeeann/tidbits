var longestCommonPrefix = function(strs) {
    let word = strs[0];
    for(let i = 1; i < strs.length; i++) {
        let built = '';
        let compareWord = strs[i];
        for(let l = 0; l < word.length; l++) {
            if(compareWord[l] === word[l]) {
                built += compareWord[l];
            } else {
                break;
            }
        }
        if(built.length < word.length) {
            word = built;
        }
    }
    return word;
};
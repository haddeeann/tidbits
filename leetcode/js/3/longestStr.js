var lengthOfLongestSubstring = function(s) {
    if(s.length === 0) {
        return 0;
    }
    let t = '';
    let longest = 1;
    let longestWord = '';
    for(let i in s) {
        if(s.slice(i).length > longest) {
            let found = findLongest(s.slice(i));
            if(found && found.length > longest) {
                longest = found.length;
                longestWord = found;
            }      
        }
    }
    
    return longest;
};

function replace(str) {
     return str.replace(/([.?*+^$[\]\\(){}|-])/g, "\\$1");
};

function findLongest(s) {
        for(let i = 0; i < s.length; i++) {
            let re = new RegExp(replace(s[i]), 'g');
            t = s.slice(0, i + 1);

            let found = t.match(re);
            if(found && found.length > 1) {
                return s.slice(0, i);
            }
        }
    
        return s;
}
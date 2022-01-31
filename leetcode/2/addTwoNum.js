var addTwoNumbers = function(l1, l2, carry = 0) {
    if(!l1 && !l2 && carry === 0) {
        return;
    }
    let digit;
    let add1 = l1 ? l1.val : 0;
    let add2 = l2 ? l2.val : 0;
    let next1 = l1 ? l1.next : null;
    let next2 = l2 ? l2.next : null;
    
    if(add1 + add2 + carry > 9) {
        digit = Number((add1 + add2 + carry).toString()[1]);
        carry = 1;
    } else {
        digit = add1 + add2 + carry;
        carry = 0;
    }
    
    return new ListNode(digit, addTwoNumbers(next1, next2, carry));
};
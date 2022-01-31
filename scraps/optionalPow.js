function optionalPow(a, b) {
  let ok = true;
  let answer = undefined;
  if(ok) {
    answer = Math.pow(a, b);
  } else {
    answer = Math.pow(b, a);
  }
  
  return answer;
}

console.log(optionalPow(0,0));
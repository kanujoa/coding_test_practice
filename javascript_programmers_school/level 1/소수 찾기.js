function isPrimeNum(num) {
  for (let d = 2; d <= Math.floor(num ** 0.5); d++) {
    if (num % d == 0) return false;
  }
  return true;
}

function solution(n) {
  let answer = 0;
  for (let num = 2; num <= n; num++) {
    if (isPrimeNum(num)) answer += 1;
  }
  return answer;
}

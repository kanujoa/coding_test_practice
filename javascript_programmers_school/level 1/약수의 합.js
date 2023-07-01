function solution(num) {
  let sum = 0;
  for (let n = 1; n <= num; n++) {
    if (num % n === 0) {
      sum += n;
    }
  }
  return sum;
}

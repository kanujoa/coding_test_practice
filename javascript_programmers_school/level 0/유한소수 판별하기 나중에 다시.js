function solution(a, b) {
  const [smaller, bigger] = [a < b ? a : b, a < b ? b : a];
  let divisor = 1;
  for (i = 2; i <= smaller; i++) {
    if (smaller % i === 0 && bigger % i === 0) {
      divisor = i;
    }
  }
  for (i = 2; i < b / divisor; i++) {
    if ((b / divisor) % i === 0) {
      if (i !== 2 || i !== 5) {
        return 2;
      }
    }
  }
  return 1;
}

console.log(solution(7, 20));
console.log(solution(11, 22));
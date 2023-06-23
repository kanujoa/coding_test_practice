function solution(number, n, m) {
  if (number % n == 0 && number % m == 0) {
    return 1;
  } else {
    return 0;
  }
}

// 간단한 풀이
// js에서는 python과 다르게 값 자체뿐만 아니라 자료형까지 비교하는 === 연산자를 사용해야 함.
const solution = (num, n, m) => (num % n === 0 && num % m === 0 ? 1 : 0);

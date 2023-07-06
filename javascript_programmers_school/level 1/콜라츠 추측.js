function Collatz(num, cnt) {
  if (num === 1) return cnt;
  else if (cnt === 500) return -1;
  else if (num % 2 === 0) return Collatz(num / 2, cnt + 1);
  else if (num % 2 === 1) return Collatz(num * 3 + 1, cnt + 1);
}

function solution(num) {
  return Collatz(num, 0);
}

// 다른 사람의 풀이
// while문 (반복문)을 사용한 코드
function collatz(num) {
  var answer = 0;
  while (num != 1 && answer != 500) {
    num % 2 == 0 ? (num = num / 2) : (num = num * 3 + 1);
    answer++;
  }
  return num == 1 ? answer : -1;
}

// 한줄로 작성하는 방법
function solution(n) {
  const answer = String(n)
    .split("")
    .reduce((sum, cur) => sum + Number(cur), 0);
  return answer;
}

// 풀어쓰기
function solution(n) {
  let answer = 0;
  for (s of String(n)) {
    answer += parseInt(s);
  }
  return answer;
}

// 다른 사람의 풀이
// n을 문자열로 바꾸는 다른 방법
// js에서는 더하기 연산에서 피연산자 중 하나가 문자열이면 숫자가 문자열로 변환되어 계산 결과가 문자열끼리 더한 값이 된다.

function solution(n) {
  return (n + "").split("").reduce((acc, curr) => acc + parseInt(curr), 0);
}

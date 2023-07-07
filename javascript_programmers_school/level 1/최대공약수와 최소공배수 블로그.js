// 유클리드 호제법

function GCD(big, small) {
  if (big % small === 0) return small;
  else return GCD(small, big % small);
}

function solution(n, m) {
  let answer = [];
  const big = Math.max(n, m),
    small = Math.min(n, m);
  answer.push(GCD(big, small));
  answer.push(answer[0] * (n / answer[0]) * (m / answer[0]));
  return answer;
}

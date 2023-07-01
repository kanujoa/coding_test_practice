function solution(a, b) {
  let sum = 0;
  for (let n = Math.min(a, b); n <= Math.max(a, b); n++) {
    sum += n;
  }
  return sum;
}

// 다른 사람의 풀이 (가우스 공식 이용, 등차수열의 합 공식과 동일)
// 양 끝의 합 * 그 사이의 수의 개수 / 2
function adder(a, b) {
  return ((a + b) * (Math.abs(a - b) + 1)) / 2;
}

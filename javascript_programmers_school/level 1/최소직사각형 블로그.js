// 명함은 돌려서 넣을 수도 있으므로 각 명함의 너비와 높이 중 작은 값과 큰 값을 구별하여 작은 값 중에서 큰 값, 큰 값 중에서 작은 값을 구해야 한다.
function solution(sizes) {
  let max = 0,
    min = 0;
  for (let size of sizes) {
    const big = Math.max(...size),
      small = Math.min(...size);
    if (big > max) max = big;
    if (small > min) min = small;
  }
  return max * min;
}

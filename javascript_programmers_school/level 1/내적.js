function solution(a, b) {
  return a.reduce((acc, cur, i) => {
    return acc + cur * b[i];
  }, 0);
}

// reduce를 사용하되 cur 인자 부분을 _로 작성하여 사용하지 않기 (인덱스만 사용하기)
function solution(a, b) {
  return a.reduce((acc, _, i) => (acc += a[i] * b[i]), 0);
}

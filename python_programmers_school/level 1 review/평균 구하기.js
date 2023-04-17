function solution(arr) {
  const total = arr.reduce((total, e) => total + e, 0);
  return total / arr.length;
}

// 풀어서 작성하기
function solution(arr) {
  let sum = 0;
  for (e of arr) {
    sum += e;
  }
  return sum / arr.length;
}

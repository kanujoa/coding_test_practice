function sort(a, b) {
  return b - a;
}

function solution(k, m, score) {
  let result = 0;
  score.sort(sort);
  for (let i = m - 1; i < score.length; i += m) {
    result += score[i] * m;
  }
  return result;
}

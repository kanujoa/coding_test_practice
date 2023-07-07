function sort(a, b) {
  return a - b;
}

function solution(d, budget) {
  d.sort(sort);
  let sum = 0;
  for (i = 0; i < d.length; i++) {
    sum += d[i];
    if (sum > budget) return i;
  }
  return d.length;
}

function sort(a, b) {
  return b - a;
}

function solution(n) {
  return Number(String(n).split("").sort(sort).join(""));
}

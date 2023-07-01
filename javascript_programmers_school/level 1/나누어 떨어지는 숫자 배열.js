function sort(a, b) {
  return a - b;
}

function solution(arr, divisor) {
  const result = arr.filter((num) => num % divisor === 0).sort(sort);
  return result.length != 0 ? result : [-1];
}

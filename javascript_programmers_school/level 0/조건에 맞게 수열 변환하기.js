function solution(arr, k) {
  const result =
    k % 2 === 1 ? arr.map((num) => num * k) : arr.map((num) => num + k);
  return result;
}

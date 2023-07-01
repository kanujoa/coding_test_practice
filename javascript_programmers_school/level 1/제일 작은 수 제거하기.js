function solution(arr) {
  // js에서는 python에서처럼 배열 자체에 min을 적용할 수 없으므로 min을 사용하려면 전재 연산자로 배열의 요소들을 전개시켜 주어야 한다.
  arr.splice(arr.indexOf(Math.min(...arr)), 1);
  return arr.length ? arr : [-1];
}

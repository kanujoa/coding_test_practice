function solution(flo) {
  return parseInt(flo.toString().split(".")[0]);
}

// 다른 사람의 풀이
// Math.floor를 사용하면 간단하게 소수점 아래 부분을 없앨 수 있다.
const solution = (flo) => Math.floor(flo);

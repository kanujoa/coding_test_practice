// substring(a, b) -> 문자열의 인덱스 a 부터 b 까지 자르기
// substring(a) -> 문자열의 인덱스 a 부터 끝까지 자르기 (substring은 무조건 끝 중심)
function solution(A, B) {
  for (let times = 0; times < A.length; times++) {
    if (A === B) {
      return times; // 문자열을 밀지 않아도 같으면 문자열을 민 times 반환
    }
    A = A.substring(A.length - 1) + A.substring(0, A.length - 1); // 문자열 밀기
  }
  return -1;
}

// 다른 사람의 풀이
let solution = (a, b) => (b + b).indexOf(a);

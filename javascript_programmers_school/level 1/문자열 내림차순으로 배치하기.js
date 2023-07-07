function solution(s) {
  return s.split("").sort().reverse().join("");
}
// JS에서 sort는 문자열로 변환 후 UTF-16 코드 유닛 값을 기준으로 정렬한다.

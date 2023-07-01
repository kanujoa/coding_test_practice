function solution(x, n) {
  let answer = [];
  for (let cnt = 1; cnt <= n; cnt++) {
    answer.push(x * cnt);
  }
  return answer;
}

// 짧은 코드
function solution(x, n) {
  return Array(n)
    .fill(x)
    .map((v, i) => (i + 1) * v);
}
// n만큼의 길이의 배열 생성 후 모든 값을 x로 채우기, 그리고 요소를 하나씩 돌면서 그 요소 * (그 요소의 인덱스값 + 1) 실행
// v는 요소 하나하나를, i는 그 요소 하나하나의 인덱스값에 해당

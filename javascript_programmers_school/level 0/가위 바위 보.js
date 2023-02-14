function solution(rsp) {
  const toWin = {
      "2": "0",
      "0": "5",
      "5": "2"
  };
  let result = "";
  for (i of rsp) {
      result += toWin[i];
  }
  return result;
}

// 코드 줄이기 (내 풀이와 같은 방법 : 객체 사용)
// function solution(rsp) {
//   let arr = {
//       2: 0,
//       0: 5,
//       5: 2
//   };
//   var answer = [...rsp].map(v => arr[v]).join("");     --> 전개 구문과 map 메서드 사용, 그로 인해 생성된 리스트 요소들을 합치는 join 메서드 사용 
//   return answer;
// }
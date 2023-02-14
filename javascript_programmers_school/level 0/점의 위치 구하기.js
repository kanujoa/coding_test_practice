function solution(dot) {
  if (dot[0] > 0) {
      const result = dot[1] > 0 ? 1 : 4;
      return result
  }
  else {
      const result = dot[1] > 0 ? 2 : 3;
      return result
  }   
}

// 짧은 풀이 (내 답안을 줄여서 아래와 같이 작성할 수 있다.)
// function solution(dot) {
//   return dot[0] > 0 ? (dot[1] > 0 ? 1 : 4) : (dot[1] > 0 ? 2 : 3);
// }


// 구조분해할당 이용
// function solution(dot) {
//   const [num,num2] = dot;     --> dot의 첫 번째 요소는 num에, 두 번째 요소는 num2에 담기게 됨.
//   const check = num * num2 > 0;     --> 둘 다 양수인지 음수인지 혹은 양수 음수가 섞여있는지 확인하기
//   return num > 0 ? (check ? 1 : 4) : (check ? 3 : 2);
// }
function solution(num_list, n) {
  var answer = [];
  const range = num_list.length / n;     // 이것은 변하면 안되는 값이므로 for문에 적어주면 안된다. (i <= num_list.length/n 이렇게 적는 것 금지!)
  for (i=1; i <= range; i++) {
      const splice = num_list.splice(0, n);     // num_list에서 첫번째 요소부터 n개 삭제한다. (아래 첫번째 예시로 보면 첫번째, 두번째 요소 삭제한다는 뜻. splice를 사용하였으므로 num_list는 옆 동작이 실행될 때마다 해당 요소들이 사라짐.)
      answer.push(splice);
  }
  return answer;
}

console.log(solution([1, 2, 3, 4, 5, 6, 7, 8], 2));
console.log(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3));
// 디버깅 종료하려면 breakpoint를 다시 클릭하여 없애주면 됨.

// 똑같은 방법, 더 간단한 풀이
// function solution(num_list, n) {
//   var answer = [];

//   while(num_list.length) {     --> while문 사용하여 num_list의 길이만큼 반복! 
//       answer.push(num_list.splice(0,n));
//   }

//   return answer;
// }
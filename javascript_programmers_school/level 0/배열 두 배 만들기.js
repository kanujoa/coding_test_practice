function solution(numbers) {
  var answer = [];
  for (let num of numbers) {     // of 대신 in을 쓰게 되면 num에는 numbers 리스트의 요소들이 아닌 인덱스들이 들어가게 되므로 사용 불가
      answer.push(num * 2)
  }
  return answer;
}

// 다른 풀이 1 (reduce 사용)
// function solution(numbers) {
//   return numbers.reduce((a, b) => [...a, b * 2], []);     --> a: 누산값, b: 현재요소값
// }

// 다른 풀이 2(map 사용)
// const solution = (numbers) => numbers.map((number) => number * 2)
// map() 메서드는 배열 내의 모든 요소를 돌면서 주어진 함수의 결과를 모아 새로운 배열을 리턴한다.


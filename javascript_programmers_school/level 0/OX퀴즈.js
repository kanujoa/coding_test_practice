function solution(quizs) {
  const scoring = [];     // O, X 결과를 담을 리스트
  for (let quiz of quizs) {     // 입력값으로 들어온 quizs 리스트의 요소 하나하나가 quiz에 대입됨.
    const quizSplit = quiz.split(" = ");     // 식 하나(quiz)에서 " = "를 기준으로 식 부분과 답 부분으로 나눔.
    const expression = quizSplit[0];     // 식 부분을 변수 expression에 대입 (위에서 " = "로 적어 주었으므로 양끝 공백을 제거하는 trim메서드를 사용하지 않아도 된다.)
    const result = parseInt(quizSplit[1]);     // 답 부분을 int형으로 바꾸어 변수 result에 대입
    const exSplit = expression.split(" ");     // 식 부분을 공백 기준으로 나눔.
    const answer = parseInt(exSplit[0]) + (exSplit[1] === "+" ? 1 : -1) * parseInt(exSplit[2]);     // 진짜 정답 구하기 
    if (answer === result) {
      scoring.push("O");
    } else {
      scoring.push("X");
    }
  }
  return scoring;
}

console.log(solution(["3 - 4 = -3", "5 + 6 = 11"]));

// 비슷한 풀이
// function solution(quiz) {
//   var answer = [];     --> O, X 결과를 담을 리스트
//   return quiz.map(t => {     --> map 메서드를 사용하여 quiz 리스트의 각 요소에 아래 코드를 적용!
//       const [calc, result] = t.split(' = ');     --> 옆과 같이 구조분해할당을 이용하면 코드가 짧아짐!
//       const sign = calc.includes('+') ? 1 : -1     --> 계산식 부분인 calc가 +를 포함하고 있다면 1을, 아니면(-를 포함하고 있다면) -1을 반환함.
//       const [a, b] = calc.split(sign === 1 ? ' + ' : ' - ');     --> 위에서 반환되어 sign에 저장된 수가 1이면 ' + '를, 아니면 ' - '를 기준으로 계산식인 calc를 나누어 리스트에 담음. 그리고 그것을 구조분해할당함.
//       return +a + (+b * sign) === +result ? 'O' : 'X'     --> 진짜 계산 결과인 a + (b * sign)이 quiz에서의 result와 같다면 'O'를, 아니면 'X'를 반환함.
//   });
// }
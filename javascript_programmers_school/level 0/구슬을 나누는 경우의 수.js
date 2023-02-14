const solution = (balls, share) => {
  let numer = 1;
  let denom = 1;
  for (i = balls; i > share; i--) {
      numer *= i;
  }
  for (i = 1; i <= balls-share; i++) {
    denom *= i;
  }
  return Math.floor(numer / denom);     // 소수점 오류 방지용
}

console.log(solution(3, 2));
console.log(solution(5, 3));

// 다른 풀이 (재귀함수 사용)
// 재귀함수는 함수가 자신을 다시 호출하는 구조로 만들어진 함수이다. 종료조건을 설정해 주지 않으면 무한반복하게 된다. (반복문으로도 작성 가능)

// const 팩토리얼 = (num) => num === 0 ? 1 : num * 팩토리얼(num - 1)     --> 3이 인자로 들어간다 치면 3 * 2 * 1 * 1 의 값이 return되게 된다.

// function solution(balls, share) {
//   return Math.round(팩토리얼(balls) / 팩토리얼(balls - share) / 팩토리얼(share))
// }

// 컴퓨터에서 0.1 + 0.2 라는 소숫점 연산을 하면 0.30000....4의 결과가 나온다.  
// 이유: 우리는 계산을 할 때 10진법을 사용하지만 컴퓨터는 2진법(0과 1만을 사용)을 사용하기 때문에 컴퓨터에서는 10진법을 2진법으로 바꾸는 과정을 거치는데 이 과정에서 소수 중 일부가 무한소수가 되어버린다.
//       but 컴퓨터 메모리에는 한계가 있어 그것을 중간에 잘라 유한 소수로 저장해 버린다. 따라서 미세한 오차가 발생한다.
// 해결 : 대부분 결과값을 소수점 12번째 자리에서 반올림하는 방법을 사용한다.
// JS에서 해결법 1: .toFixed() 후 Number()     --> 소수점 특정 자리까지 반올림 후 숫자 형태로 바꾸기
// Js에서 해결법 2: Math.round()     --> 반올림(정수값 반환)
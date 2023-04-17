// num이 음수인 경우도 있음에 주의하자!
// 조건 연산자(삼항 연산자)를 사용한 풀이
function solution(num) {
  return Math.abs(num % 2) === 1 ? "Odd" : "Even";
}

// 좀 더 짧은 풀이
// num % 2의 결과가 0이 아닐 경우(참일 경우) Odd, 결과가 1일 경우(거짓일 경우) Even
// * 음수의 경우 아래와 같이 연산을 하면 나머지가 -0 or -1이 나온다. -0은 0과 완전히 같다.(===)
function evenOrOdd(num) {
  return num % 2 ? "Odd" : "Even";
}

function solution(n) {
  const factorial = (num) => num === 0 ? 1 : num * factorial(num - 1);     // 재귀 함수 이용하여 factorial 값을 구하는 과정을 작성함. (n이 3이라면 3 * 2 * 1 * 1의 순서로 계산됨.)
  for (i = 0; i <= 11; i++) {     // i는 factorial 함수의 인자로 들어갈 것임. n의 최대값이 362800으로 정해졌으므로 result의 최대값은 10이고, 이를 맞추기 위해 i는 11보다 같거나 같음으로 작성해 줌.
    if (factorial(i) > n) {     // factorial에 i를 대입하여 계산한 값이 n보다 크면
        return i - 1;     // 그것보다 작은 정수를 출력해야 하므로 -1을 한 값을 return함.
    } 
  }
}

console.log(solution(3628800));
console.log(solution(7));

// 다른 풀이
// function solution(n) {
//   let i = 1;     
//   let f = 1;
//   while (f*i < n) f*=++i;      --> ++i로 적어주면 f에 1이 증가된 i값을 곱해주면서 동시에 i값도 1 증가된다. (결국 f 값은 팩토리얼 계산을 실행한 값이 됨.)
//   return i;
// }

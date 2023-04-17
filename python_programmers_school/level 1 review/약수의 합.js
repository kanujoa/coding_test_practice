function solution(n) {
  if (n === 0) {
    // n이 0인 경우와
    return 0;
  } else if (n === 1) {
    // n이 1인 경우는 따로 처리
    return 1;
  } else {
    // n이 2 이상인 경우
    let answer = 0;
    for (let divisor = 2; divisor <= Math.floor(n / 2); divisor++) {
      if (n % divisor === 0) {
        answer += divisor;
      }
    }
    return answer + 1 + n;
  }
}

// 위 코드를 아래와 같이 작성해도 문제없다.
// n이 1이나 0일 경우 divisor <= Math.floor(n/2) 조건에서 이미 false가 되어 반복문은 실행되지 않고 넘어간다.
function solution(n) {
  let answer = 0;
  for (let divisor = 1; divisor <= Math.floor(n / 2); divisor++) {
    if (n % divisor === 0) {
      answer += divisor;
    }
  }
  return answer + n;
}

// 다른 사람의 더 간단한 풀이
// 위 문제에서 아래 방식으로 해 주는 것이 더 빠르다.
function solution(num) {
  let sum = 0;
  for (let i = 1; i <= num; i++) {
    if (num % i === 0) sum += i;
  }
  return sum;
}

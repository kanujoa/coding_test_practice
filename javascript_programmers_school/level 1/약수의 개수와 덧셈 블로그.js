const DivisorCnt = (n) => {
  let cnt = 0;
  for (let i = 1; i <= Math.floor(n / 2); i++) {
    if (n % i == 0) cnt += 1;
  }
  return Number.isInteger(n ** 0.5) ? cnt * 2 - 1 : cnt * 2;
};

function solution(left, right) {
  let answer = 0;
  for (let n = left; n <= right; n++) {
    const cnt = DivisorCnt(n);
    cnt % 2 ? (answer -= n) : (answer += n);
  }
  return answer;
}

// 사실 약수의 개수를 직접적으로 다 구하지 않아도 된다. 약수의 개수가 짝수인지 홀수인지만 판단하면 되므로!
// 제곱근이 정수일 경우에만 약수가 홀수개이다. 약수는 항상 다른 수와 짝지어져 나오므로
function solution(left, right) {
  var answer = 0;
  for (let i = left; i <= right; i++) {
    if (Number.isInteger(Math.sqrt(i))) {
      // Math.sqrt는 제곱근을 반환한다. (square root)
      answer -= i;
    } else {
      answer += i;
    }
  }
  return answer;
}

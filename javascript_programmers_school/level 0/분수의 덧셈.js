// 유클리드 호제법 이용해 최대공약수 구하기
// 유클리드 호제법에서 꼭 a가 b보다 큰 수여야 하는 것은 아니다. 크기 상관 없이 적어줄 수 있으므로
// Math.max와 min을 사용할 필요 X
function GCD(a, b) {
  if (a % b === 0) {
    return b;
  } else {
    return GCD(b, a % b);
  }
}

function solution(numer1, denom1, numer2, denom2) {
  var result = [numer1 * denom2 + numer2 * denom1, denom1 * denom2];
  var gcd = GCD(Math.max(result[0], result[1]), Math.min(result[0], result[1]));
  result[0] /= gcd;
  result[1] /= gcd;
  return result;
}

// 최대공약수 구하는 코드를 좀 더 간단하게 나타낸 풀이 (삼항 연산자로 재귀 작성)
function fnGCD(a, b) {
  return a % b ? fnGCD(b, a % b) : b;
}

function solution(denum1, num1, denum2, num2) {
  let denum = denum1 * num2 + denum2 * num1;
  let num = num1 * num2;
  let gcd = fnGCD(denum, num); //최대공약수

  return [denum / gcd, num / gcd];
}

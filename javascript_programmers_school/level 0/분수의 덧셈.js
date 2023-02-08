function solution(numer1, denom1, numer2, denom2) {
  let denom = denom1 * denom2;     // 분수의 덧셈법을 이용한 분자, 분모 정의
  let numer = numer1 * denom2 + numer2 * denom1;
  for (let i = Math.min.apply(null, [denom, numer]); i > 0; i--) {     // 분자, 분모의 최대공약수 구하기 (따라서 큰 수부터 살펴봄.)
      if (denom % i === 0 && numer % i === 0) {
          denom = denom / i;     // 최종 분자, 분모는 둘의 최대공약수로 약분한 것!
          numer = numer / i;
          break;     // 최대공약수 구하면 바로 for문 빠져나오기
      }
  }
  return [numer, denom];     // 결과는 둘 다 int 형태로 list에 담겨 있어야 한다. (string 형태이면 오류남!)
}

// 다른 풀이
// function fnGCD(a, b){
//   return (a%b)? fnGCD(b, a%b) : b;
// }

// function solution(denum1, num1, denum2, num2) {
//   let denum = denum1*num2 + denum2*num1;
//   let num = num1 * num2;
//   let gcd = fnGCD(denum, num); //최대공약수

//   return [denum/gcd, num/gcd];
// }
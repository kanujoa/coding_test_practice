function GCD(a, b) {
  if (a % b === 0) {
    return b;
  } else {
    return GCD(b, a % b);
  }
}

function Judge(b) {
  while (b % 2 === 0) {
    b /= 2;
  }
  while (b % 5 === 0) {
    b /= 5;
  }
  if (b === 1) return 1;
  else return 2;
}

function solution(a, b) {
  const gcd = GCD(a, b);
  b /= gcd;
  return Judge(b);
}

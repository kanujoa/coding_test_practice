function solution(a, b, n) {
  let coke = 0;
  while (n >= a) {
    coke += Math.floor(n / a) * b;
    // 받을 콜라병 수를 계산할 때 뿐만 아니라 현재 남은 콜라병 수를 계산할 때에도 b를 고려해 주어야 한다!
    n = Math.floor(n / a) * b + (n % a);
  }
  return coke;
}

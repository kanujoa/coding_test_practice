function solution(price, money, count) {
  let need = 0;
  for (let cnt = 1; cnt <= count; cnt++) {
    need += price * cnt;
  }
  return money - need >= 0 ? 0 : need - money;
}
// 가지고 있는 돈이 필요한 돈보다 많을 경우도 있을 수 있으므로 return need - money 할 게 아니라 옆 경우도 생각해 주어야 함.

// 다른 사람의 코드 (가우스 공식 이용, 등차수열의 합 생각)
function solution(price, money, count) {
  const tmp = (price * count * (count + 1)) / 2 - money;
  return tmp > 0 ? tmp : 0;
}

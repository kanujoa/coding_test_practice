function solution(money) {
  let result = [0, 0];
  result[0] = Math.floor(money / 5500);
  result[1] = money - 5500 * result[0];
  return result
}

// 한 줄로 작성하기
// function solution(money) {
//   return [Math.floor(money / 5500), money % 5500];
// }
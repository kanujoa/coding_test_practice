function solution(price) {
  if (price >= 500000) {
      return Math.floor(price * 0.8);
  }
  else if (price >= 300000) {
      return Math.floor(price * 0.9);
  }
  else if (price >= 100000) {
      return Math.floor(price * 0.95);
  }
  else {
      return Math.floor(price);
  }
}

// 조건문 더 간단하게 작성하기
// function solution(price) {
//   if (price >= 500000)
//       return parseInt(price*(1-0.2));

//   if (price >= 300000)
//       return parseInt(price*(1-0.1));

//   if (price >= 100000)
//       return parseInt(price*(1-0.05));  

//   return price
// }

// 다른 풀이 (반복문 이용)
// const discounts = [
//   [500000, 20],
//   [300000, 10],
//   [100000, 5],
// ]

// const solution = (price) => {
//   for (const discount of discounts)
//       if (price >= discount[0])
//           return Math.floor(price - price * discount[1] / 100)
//   return price
// }
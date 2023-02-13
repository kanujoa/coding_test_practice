function solution(numbers) {
  let sum = 0;
  numbers.forEach(num => {     // for...of로도 사용 가능
      sum += num;
  });
  return sum / numbers.length;
}

// 다른 풀이 (reduce 이용!)
// function solution(numbers) {
//   return numbers.reduce((acc, cur) => acc + cur) / numbers.length
// }
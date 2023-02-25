function solution(bin1, bin2) {
  const sum = parseInt(parseInt(bin1), 2) + parseInt(parseInt(bin2), 2);     // 입력값들(이진수)을 10진수로 바꾸어 더한 값을 먼저 구하기 (parseInt 함수 사용)
  return sum.toString(2);     // 더한 값을 toString 메서드로 이진수로 바꾼다.
}

// 이진수 구현 로직
// function solution(bin1, bin2) {
//   let temp = Number(bin1) + Number(bin2);
//   temp = [...temp.toString()].reverse().map((v) => +v);

//   for (let i = temp.length; i < 11; i++) {
//     temp.push(0);
//   }

//   for (let i = 0; i < temp.length; i++) {
//     if (temp[i] === 2) {
//       temp[i] = 0;
//       temp[i + 1]++;
//     } else if (temp[i] === 3) {
//       temp[i] = 1;
//       temp[i + 1]++;
//     }
//   }
//   return Number(temp.reverse().join("")).toString();
// }
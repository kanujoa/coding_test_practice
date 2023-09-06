const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

// 상근이가 가지고 있는 숫자 카드들에 적혀 있는 수 (배열)
const nums = input[1].trim().split(" ");
// 숫자 카드인지 아닌지를 구해야 할 수들 (배열)
const haveToCheckNums = input[3].trim().split(" ");

// 카드 존재 여부를 기록할 배열 (존재하면 1, 존재하지 않으면 0으로 기록)
const result = [];

// 숫자 카드의 숫자를 기록하기 위한 record
const record = {};
for (let num of nums) {
  record[num] = 1;
}

// haveToCheckNums 배열의 수를 하나씩 차례로 순회하며 record에 해당 숫자가 있는지 확인하고, 있으면 result에 '1' push,
// 없으면 result에 '0' push
for (let num of haveToCheckNums) {
  if (!record[num]) result.push("0");
  else result.push("1");
}

console.log(result.join(" "));
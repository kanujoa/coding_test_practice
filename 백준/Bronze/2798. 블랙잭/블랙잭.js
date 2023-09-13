const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
input = [
  ...input[0].split(" ").map((item) => +item.trim()),
  input[1].split(" ").map((item) => +item),
];

const n = input[0];
const m = input[1];
const cards = input[2];
let max = 0;

function combination(arr, selNum) {
  if (selNum === 1) return arr.map((v) => [v]);
  const result = [];
  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const comb = combination(rest, selNum - 1);
    const comb_arr = comb.map((c) => [fixed, ...c]);
    result.push(...comb_arr);
  });
  return result;
}

// cards 배열에 있는 숫자들 중 3개를 골라야 한다.
const allCase = combination(cards, 3);
for (let arr of allCase) {
  const sum = arr.reduce((acc, cur) => acc + cur);
  if (sum <= m && sum > max) max = sum;
}

console.log(max);
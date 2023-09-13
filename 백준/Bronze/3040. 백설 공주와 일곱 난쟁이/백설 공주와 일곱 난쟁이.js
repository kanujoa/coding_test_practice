const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((num) => +num);

function combination(arr, selNum) {
  const result = [];
  if (selNum === 1) return arr.map((v) => [v]);

  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const comb = combination(rest, selNum - 1);
    const comb_arr = comb.map((c) => [fixed, ...c]);
    result.push(...comb_arr);
  });

  return result;
}

const allCase = combination(input, 7);
for (let arr of allCase) {
  const sum = arr.reduce((acc, cur) => acc + cur);
  if (sum === 100) {
    console.log(arr.map((num) => "" + num).join("\n"));
    break;
  }
}
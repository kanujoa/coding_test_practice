const fs = require("fs");

const [n, ...serial] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.trim());

function sortFunc(a, b) {
  if (a.length !== b.length) {
    return a.length - b.length;
  } else {
    const a_sum = sum(a);
    const b_sum = sum(b);
    if (a_sum !== b_sum) return a_sum - b_sum;
    else return a.localeCompare(b);
  }
}

function sum(string) {
  const sum_result = string.split("").reduce((acc, cur) => {
    if (+cur == cur) acc += +cur;
    return acc;
  }, 0);
  return sum_result;
}

serial.sort(sortFunc);
console.log(serial.join("\n"));
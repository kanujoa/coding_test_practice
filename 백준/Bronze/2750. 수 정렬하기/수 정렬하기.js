const fs = require("fs");
const array = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((num) => +num);

const resultArr = array.slice(1, array.length).sort((a, b) => a - b);
console.log(resultArr.map((num) => String(num)).join("\n"));
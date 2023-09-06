const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const array = input.slice(1, input.length).map((str) => str.trim());
array.sort((a, b) => {
  const aAge = Number(a.split(" ")[0]);
  const bAge = Number(b.split(" ")[0]);
  return aAge - bAge;
});

console.log(array.join("\n"));
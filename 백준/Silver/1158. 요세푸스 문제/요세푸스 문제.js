const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [ a, b ] = input[0].split(' ');

let answer = [];
let numArray = [];

for (let num = 1; num <= a; num++) {
  numArray.push(num);
}

while (numArray.length > 0) {
  for (let i = 1; i < b; i++) {
    numArray.push(numArray.shift());
  }
  answer.push(numArray.shift());
}

console.log(`<${answer.join(", ")}>`);


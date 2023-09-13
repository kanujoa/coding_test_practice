const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((num) => +num);

const [n, m] = input;
const ch = Array(n + 1).fill(0);
const pick = Array(m).fill(0);
const result = [];

function permutation(l) {
  if (l === m) {
    result.push(pick.join(" "));
  } else {
    for (let i = 1; i <= n; i++) {
      if (ch[i] === 0) {
        ch[i] = 1;
        pick[l] = i;
        permutation(l + 1);
        ch[i] = 0;
      }
    }
  }
}

permutation(0);
console.log(result.join("\n"));

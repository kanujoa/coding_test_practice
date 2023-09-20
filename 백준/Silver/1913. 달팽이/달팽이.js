const fs = require("fs");
const [n, numToFindPos] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => +item);

const result = Array.from(Array(n), () => Array(n).fill(0));

let num = 1;
// 순서대로 up, right, down, left로 이동할 때 인덱스에 적용할 숫자
let moves = [-1, 1, 1, -1];
// 위 이동을 얼마만큼 반복해야 하는지에 대한 숫자
let times = [1, 1, 2, 2];
let row = (n - 1) / 2;
let col = (n - 1) / 2;
let pos = [row + 1, col + 1];
result[row][col] = num;
num++;

while (num <= n * n) {
  // 한 바퀴 돌기 (한 세트)
  outer: for (let times_idx = 0; times_idx < 4; times_idx++) {
    const time = times[times_idx];
    for (let t = 0; t < time; t++) {
      if (times_idx % 2 === 0) row += moves[times_idx];
      else col += moves[times_idx];
      result[row][col] = num;
      if (num === numToFindPos) {
        pos[0] = row + 1;
        pos[1] = col + 1;
      }
      num++;
      if (num > n * n) break outer;
    }
  }
  times = times.map((time) => time + 2);
}

const tmp = [];
for (let arr of result) {
  arr = arr.map((item) => "" + item);
  tmp.push(arr.join(" "));
}
tmp.push(pos.map((item) => "" + item).join(" "));
console.log(tmp.join("\n"));
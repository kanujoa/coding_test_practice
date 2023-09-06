const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const arr = input.slice(1, input.length).map((num) => +num);

let record = {};
let cnt = 0;

function WayCnt(num, acc) {
  if (acc === num) {
    cnt += 1;
    return;
  } else if (acc > num) {
    return;
  } else {
    WayCnt(num, acc + 1);
    WayCnt(num, acc + 2);
    WayCnt(num, acc + 3);
  }
}

for (let num of arr) {
  for (let i = 1; i <= num; i++) {
    if (i <= 3) {
      WayCnt(i, 0);
      record[i] = cnt;
      cnt = 0;
    } else {
      record[i] = record[i - 1] + record[i - 2] + record[i - 3];
    }
  }
}

const result = [];
for (num of arr) {
  result.push(record[num]);
}
console.log(result.join("\n"));
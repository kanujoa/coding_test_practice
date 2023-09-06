const input = Number(require("fs").readFileSync("/dev/stdin"));

const record = Array(input + 1).fill(Infinity);
record[input] = 0;

for (let num = input; num >= 1; num--) {
  if (num % 3 === 0)
    record[num / 3] = Math.min(record[num / 3], record[num] + 1);
  if (num % 2 === 0)
    record[num / 2] = Math.min(record[num / 2], record[num] + 1);
  record[num - 1] = Math.min(record[num - 1], record[num] + 1);
}

console.log(record[1]);
const array = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const queue = [];
const result = [];

for (let i = 1; i <= array[0]; i++) {
  const command = array[i].split(" ")[0].trim();
  const num = array[i].split(" ")[1];

  if (command === "push") queue.push(num);
  else if (command === "pop") {
    if (queue.length === 0) result.push("-1");
    else result.push(queue.shift());
  } else if (command === "size") result.push(queue.length);
  else if (command === "empty") result.push(Number(queue.length === 0));
  else if (command === "front") {
    if (queue.length === 0) result.push("-1");
    else result.push(queue[0]);
  } else if (command === "back") {
    if (queue.length === 0) result.push("-1");
    else result.push(queue[queue.length - 1]);
  }
}
console.log(result.join("\n"));
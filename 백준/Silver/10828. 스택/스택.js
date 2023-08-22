const array = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const result = [];
const stack = [];

for (let i = 1; i < array.length; i++) {
  const command = array[i].split(" ");
  if (command[0] === "push") stack.push(command[1]);
  else if (command[0] === "top") {
      if (stack.length === 0) result.push('-1');
      else result.push(''+stack[stack.length - 1])
  }
  else if (command[0] === "size") result.push(''+stack.length);
  else if (command[0] === "empty") result.push(''+Number(!stack.length));
  else if (command[0] === "pop")
    if (stack.length === 0) result.push('-1')
    else result.push(stack.pop());
}

console.log(result.join('\n'));
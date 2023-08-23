const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const num = Number(input[0]);

const queue = [];

let front = 0,
  rear = num - 1;

let cnt = 0;

for (let n = 1; n <= num; n++) {
  queue.push(n);
}

while (cnt < num - 1) {
  // 첫 번째 요소 없애기 (front 포인터 1 증가)
  front++;
  // queue의 맨 마지막에 그 다음 요소 추가하기
  queue.push(queue[front]);
  // queue의 마지막으로 요소를 옮겼으므로 front 포인터 또 1 증가
  front++;
  // 마지막에 요소가 추가되었으므로 rear 포인터 1 증기
  rear++;
  cnt++;
}

console.log(queue[rear]);
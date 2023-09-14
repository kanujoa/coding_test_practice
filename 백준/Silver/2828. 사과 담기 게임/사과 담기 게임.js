const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// n : 스크린 칸의 수, m : 바구니가 차지하는 칸의 수
const [n, m] = input[0].split(" ").map((item) => Number(item.trim()));
// 사과가 떨어지는 위치
const applePos = input.slice(2).map((pos) => Number(pos.trim()));

// 현재 바구니의 왼쪽 끝과 오른쪽 끝의 위치 (처음에는 스크린의 왼쪽 끝에 놓여 있음.)
let l = 1;
let r = m;
// 바구니를 옮길 때 최소 이동 칸 수
let result = 0;

for (let pos of applePos) {
  // 사과가 떨어지는 자리에 바구니가 위치해 있다면 바구니를 옮길 필요가 없으므로 그냥 건너뛰기
  if (pos >= l && pos <= r) continue;
  // 사과가 떨어지는 자리가 바구니 위치보다 더 오른쪽이라면 바구니의 오른쪽 끝을 사과가 떨어지는 위치에 맞춘다.
  else if (pos > r) {
    result += pos - r;
    r = pos;
    l = r - m + 1;
  }
  // 사과가 떨어지는 자리가 바구니 위치보다 더 왼쪽이라면 바구니의 왼쪽 끝을 사과가 떨어지는 위치에 맞춘다.
  else if (pos < l) {
    result += l - pos;
    l = pos;
    r = l + m - 1;
  }
}

console.log(result);
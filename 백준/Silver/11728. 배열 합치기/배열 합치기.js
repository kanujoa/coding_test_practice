const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 배열 a의 크기와 배열 b의 크기를 입력받음
const [aSize, bSize] = input[0].split(" ").map((num) => +num);
// 배열 a 입력받기 (정렬되어 있음)
const a = input[1].split(" ").map((num) => +num);
// 배열 b 입력받기 (정렬되어 있음)
const b = input[2].split(" ").map((num) => +num);

// 정렬 결과를 담기 위한 배열
let result = [];

// a 배열에 사용할 인덱스와 b 배열에 사용할 인덱스를 정의
let aIdx = 0;
let bIdx = 0;

// aIdx가 aSize보다 작으면서 bIdx가 bSize보다 작을 때까지 아래 코드 반복
while (aIdx < aSize && bIdx < bSize) {
  // a에서의 원소가 b에서의 원소보다 더 크면 작은 원소를 result 배열에 먼저 넣어야 하므로 b에서의 원소를 push
  // bIdx 1 증가
  if (a[aIdx] >= b[bIdx]) {
    result.push(b[bIdx]);
    bIdx++;
    // 반대일 경우 더 작은 원소가 a에서의 원소이므로 그것을 result 배열에 넣기
    // aIdx 1 증가
  } else {
    result.push(a[aIdx]);
    aIdx++;
  }
}

// 두 배열 중 하나의 배열의 순회가 먼저 끝나므로 순회가 아직 끝나지 않은 배열의 남은 숫자들을 result 배열에 그대로 넣어줌.
// 이미 정렬되어 있으므로!
result =
  aIdx !== aSize
    ? [...result, ...a.slice(aIdx, aSize)]
    : [...result, ...b.slice(bIdx, bSize)];

console.log(result.map((num) => "" + num).join(" "));
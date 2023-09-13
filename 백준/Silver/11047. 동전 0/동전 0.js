const fs = require("fs");
// 입력 받을 때 우선 띄어쓰기 기준으로 split하여 나눔.
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
// 그 다음 \n을 기준으로 split하고, 그것을 전개 연산자를 통해 배열 하나에 넣는 것으로 바꾸기
input = [
  Number(input[0]),
  ...input[1].split("\n").map((item) => {
    item.trim();
    return Number(item);
  }),
];

// 만들어야 할 가치의 합 (계산하면서 변할 것임)
let k = input[1];
// 동전의 종류 합
const n = input[0];
// 동전의 종류 배열
const coins = input.slice(2);
// 필요한 동전 개수의 최솟값
let need = 0;

// 큰 단위의 동전부터 최대로 사용하여 k의 값을 만든다.
// coins 배열을 거꾸로 정렬하면 그 시간이 드므로 그냥 인덱스를 끝에서부터 시작한다.
for (let i = n - 1; i >= 0; i--) {
  // 현재 동전의 단위가 만들어야 할 가치인 k보다 크면 건너뛰어 더 작은 단위로 가기
  if (coins[i] > k) continue;
  // k를 현재 동전 단위로 나눈 몫만큼이 필요한 동전 개수에 포함됨.
  need += Math.floor(k / coins[i]);
  // 이미 만든 부분은 제외해야 하므로 k에서 이미 만든 값은 빼주기
  k -= coins[i] * Math.floor(k / coins[i]);
}

console.log(need);
const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();

// 결과를 최소로 만들기 위해서는 덧셈을 모두 먼저 처리한 후 빼기를 진행해야 한다.
// '-'를 기준으로 나누면 더하기를 수행해야 하는 두 수가 하나로 묶여서 나온다.
input = input.split("-");
input = input.map((item) => {
  // '+'가 있는 item의 경우 '+'를 기준으로 나누어 Number로 형변환 후 더한 값을 반환
  // 0으로 시작하는 숫자는 Number 형변환을 통해 앞의 0들은 사라지게 됨.
  if (item.includes("+")) {
    item = item.split("+");
    return item.reduce((acc, cur) => acc + +cur, 0);
    // 그렇지 않고 그냥 숫자만 있는 경우 연산을 하지 않고 그냥 Number 형으로만 바꾸어 반환
  } else return +item;
});

// 위 과정을 마치면 - 연산할 것들만 남으므로 reduce를 이용해 빼기 연산을 누적하며 진행하면 된다.
// 더하기만 있었던 경우에는 아래 빼기 연산이 이루어지지 않는다. (원소가 하나가 되므로)
console.log(input.reduce((acc, cur) => acc - cur));
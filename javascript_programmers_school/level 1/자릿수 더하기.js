function solution(n) {
  n = String(n)
    .split("")
    .map((num) => Number(num));
  return n.reduce((acc, num) => acc + num); // 초깃값으로 0을 적어주지 않으면 string이 초깃값이 된다.
}

// 더 간단히 작성하기
function solution(n) {
  // 쉬운방법
  return (n + "").split("").reduce((acc, curr) => acc + parseInt(curr), 0);
}

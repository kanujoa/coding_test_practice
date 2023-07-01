function solution(x) {
  const sum = (x + "").split("").reduce((acc, cur) => acc + Number(cur), 0);
  return x % sum ? false : true;
}

// 숫자로 접근하는 방법이 더 빠르기는 하다.
function solution(x) {
  let num = x;
  let sum = 0;
  do {
    sum += x % 10;
    x = Math.floor(x / 10);
  } while (x > 0);

  return !(num % sum);
}

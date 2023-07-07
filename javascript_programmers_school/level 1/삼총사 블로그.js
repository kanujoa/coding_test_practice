function solution(number) {
  let cnt = 0;
  for (let x = 0; x <= number.length - 3; x++) {
    for (let y = x + 1; y <= number.length - 2; y++) {
      for (let z = y + 1; z <= number.length - 1; z++) {
        if (number[x] + number[y] + number[z] === 0) cnt += 1;
      }
    }
  }
  return cnt;
}

// 다른 사람의 풀이 (보고 넘어가기)
function solution(number) {
  let result = 0;

  const combination = (current, start) => {
    if (current.length === 3) {
      result += current.reduce((acc, cur) => acc + cur, 0) === 0 ? 1 : 0;
      return;
    }

    for (let i = start; i < number.length; i++) {
      combination([...current, number[i]], i + 1);
    }
  };
  combination([], 0);
  return result;
}

function solution(numbers) {
  const pick = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].filter(
    (num) => numbers.includes(num) === false
  );
  return pick.reduce((acc, cur) => acc + cur);
}

// 다른 사람의 풀이
// 배열에 없는 숫자의 합을 구하는 것이므로 0부터 9까지 숫자의 합에서 배열에 있는 모든 숫자를 빼는 방식으로 작성하면 코드가 더 깔끔해진다.
function solution(numbers) {
  return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}

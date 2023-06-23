function solution(numbers, n) {
  let result = 0;
  for (let num of numbers) {
    if (result <= n) {
      // n보다 커지는 순간 지금까지 더한 값을 return 해야 하므로 현재 result(누적된 값)가 n보다 작거나 같을 때까지는 숫자를 더 더해도 됨.
      result += num;
    } else break;
  }
  return result;
}

// 다른 사람의 풀이
// reduce를 아래와 같은 방식으로 사용 가능함.
function solution(numbers, n) {
  return numbers.reduce((a, c, i, t) => (a <= n ? a + c : a)); // 누적된 값이 n보다 작거나 같으면 숫자를 더해주고, 누적된 값이 n보다 커지면 계속 그 값 그대로 가져감.
}

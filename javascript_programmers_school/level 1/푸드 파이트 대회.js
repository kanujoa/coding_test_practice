function solution(food) {
  let result = "0";
  for (let i = food.length - 1; i >= 1; i--) {
    const half = Math.floor(food[i] / 2);
    result = String(i).repeat(half) + result + String(i).repeat(half);
  }
  return result;
}

// 비슷한 풀이
function solution(food) {
  let res = "";
  for (let i = 1; i < food.length; i++) {
    res += String(i).repeat(Math.floor(food[i] / 2)); // 문자열 더하기는 오른쪽(반쪽)에만 우선 실행
  }

  return res + "0" + [...res].reverse().join(""); // 마지막에 res와 0을 더해주고, 뒤에는 res를 뒤집은 문자열을 더해줌.
}

function solution(arr) {
  result = [];
  arr.map((item) => {
    for (i = 0; i < item; i++) {
      result.push(item);
    }
  });
  return result;
}

// 다른 사람의 풀이
function solution(arr) {
  return arr.reduce((list, num) => [...list, ...new Array(num).fill(num)], []); // 맨 마지막에 있는 []는 초깃값
}

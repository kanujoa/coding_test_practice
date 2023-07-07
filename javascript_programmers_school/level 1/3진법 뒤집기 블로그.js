function solution(n) {
  let tenary_num = "";
  while (n !== 0) {
    tenary_num += String(n % 3);
    n = Math.floor(n / 3);
  }
  return parseInt(tenary_num, 3);
}

// 다른 사람의 풀이 (toString(진법) 메서드 사용)
const solution = (n) => {
  return parseInt([...n.toString(3)].reverse().join(""), 3);
};

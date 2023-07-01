function solution(n) {
  let i = 1;
  while (true) {
    if (n % i === 1) return i;
    else i += 1;
  }
}

// 다른 사람의 풀이
// x의 초깃값은 1로 설정
function solution(n, x = 1) {
  // while에서 증감이 가능
  // 후위 연산자이므로 다음번에 x에 1이 증가된 상태가 됨.
  while (x++) {
    // 여기에서 x가 1이 증가된 상태가 됨. 어차피 x = 1일 때는 모든 경우에서 나머지가 1이 나오는 것이 불가하므로 2부터 시작
    if (n % x === 1) {
      return x;
    }
  }
}

// 재귀도 가능
function solution(n, x = 0) {
  return n % x === 1 ? x : solution(n, x + 1);
}

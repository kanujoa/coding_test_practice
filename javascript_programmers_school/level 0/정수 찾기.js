function solution(num_list, n) {
  for (let num of num_list) {
    if (n === num) {
      return 1;
    }
  }
  return 0;
}
// js에서는 항상 type까지 똑같아야 같은 것이다. (pyhton에서처럼 조건을 그냥 n in num_list로 하면 틀림.)

// 다른 사람의 풀이 (include 메서드 사용)
const solution = (l, n) => +l.includes(n);
// +true -> 1, +false -> 0
// +!true -> 0, +!false -> 1
// !true -> false, !false -> true

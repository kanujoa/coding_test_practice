function solution(num_list) {
  const answer =
    num_list.length >= 11
      ? num_list.reduce((acc, cur) => acc + cur)
      : num_list.reduce((acc, cur) => acc * cur);
  return answer;
}
// array.length(배열의 길이를 구할 때) 뒤에 ()를 적지 않는다.

// 다른 사람의 풀이
const solution = (n) => n.reduce((a, v) => (n.length > 10 ? a + v : a * v));
// 이렇게 reduce 메서드 안에서 삼항연산자를 적어주어도 된다.

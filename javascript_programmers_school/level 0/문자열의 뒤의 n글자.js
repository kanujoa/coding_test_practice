// python에서처럼 [::]을 이용해 문자열 슬라이싱을 하면 에러 난다.
function solution(my_string, n) {
  my_array = my_string.split("");
  return my_array.slice(-n).join("");
}

// 다른 풀이
// 문자열을 자를 때는 substring 메서드를 사용할 수 있다.
// 아래의 경우 my_string의 전체 길이에서 n만큼을 빼서 그 이후의 글자만 남도록 한 것이다.
function solution(my_string, n) {
  return my_string.substring(my_string.length - n);
}

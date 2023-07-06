function solution(phone_number) {
  return (
    Array(phone_number.length - 4)
      .fill("*")
      .join("") + phone_number.slice(-4)
  );
}

// 다른 사람의 풀이 1
// repeat 메서드를 사용하면 python에서의 '*' * (s.length - 4)의 효과를 낼 수 있다.
function hide_numbers(s) {
  var result = "*".repeat(s.length - 4) + s.slice(-4);
  return result;
}

// 다른 사람의 풀이 2 (정규식 사용)
function hide_numbers(s) {
  return s.replace(/\d(?=\d{4})/g, "*");
}

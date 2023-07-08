// 정규 표현식과 replace 사용한 풀이
function solution(s) {
  const match = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };
  for (num in match) {
    const regexAllCase = new RegExp(num, "g");
    s = s.replace(regexAllCase, match[num]);
    console.log(s);
  }
  return +s;
}
// JS에서 replace는 한 글자만 가능하기 때문에 해당하는 모든 문자를 대체하고 싶다면 정규 표현식을 사용해야 함.
// 또, 정규 표현식 사용 시 변수명을 넣으면 그 변수명 자체를 찾기 때문에 new RegExp 객체를 생성하여 변수에 저장된 값을 찾게 함.

// 다른 사람의 풀이 (정규 표현식 사용 X)
function solution(s) {
  let numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  var answer = s;

  for (let i = 0; i < numbers.length; i++) {
    let arr = answer.split(numbers[i]);
    answer = arr.join(i);
  }

  return Number(answer);
}

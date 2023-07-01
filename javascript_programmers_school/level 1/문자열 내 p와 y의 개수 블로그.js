function solution(s) {
  let p_cnt = 0;
  let y_cnt = 0;
  s.toLowerCase()
    .split("")
    .map((letter) => {
      if (letter == "p") p_cnt += 1;
      else if (letter == "y") y_cnt += 1;
    });
  return p_cnt === y_cnt ? true : false;
}

// 다른 사람의 풀이
// 1. reduce를 사용하는 방법
function solution(s) {
  return [...s.toLowerCase()].reduce((acc, cur) => {
    if (cur === "p") return acc + 1;
    else if (cur === "y") return acc - 1;
    return acc;
  }, 0)
    ? false
    : true;
}

// 2. 발상의 전환
// "P"를 기준으로 s를 나눈 길이와 "Y"를 기주능로 s를 나눈 길이가 같으면 true
// "P"와 "Y"를 기준으로 나누면 그 배열에는 "P"와 "Y"는 들어 있지 않고 그 외의 잘라진 문자열로 구성되어 있다.
// P와 Y의 개수가 같아야 문자열이 등분되는 개수도 같으므로 (잘라진 문자열의 개수도 같으므로) 길이를 비교
function numPY(s) {
  return (
    s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length
  );
}

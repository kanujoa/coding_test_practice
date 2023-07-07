function solution(s) {
  for (let item of s) {
    if (Number.isInteger(+item) === false) return false;
  }
  return s.length === 4 || s.length === 6 ? true : false;
}

// 다른 사람의 풀이 (정규식)
function solution(s) {
  var result = false;
  if ((s.length == 4 || s.length == 6) && /^[0-9]+$/.test(s)) {
    result = true;
  }

  return result;
}

function solution(arr) {
  let answer = [];
  for (let num of arr) {
    if (answer.length === 0) answer.push(num);
    else if (answer[answer.length - 1] !== num) answer.push(num);
    // JS에서는 인덱싱 시 음수를 기재하는 것이 불가능하다.
  }
  return answer;
}

// 다른 사람의 풀이 (filter 사용)
function solution(arr) {
  return arr.filter((val, index) => val != arr[index + 1]);
  // 현재 값과 다음 인덱스의 값이 다를 때만 수 추출
  // 마지막 과정에서는 참조할 요소가 없기 때문에 undefined가 뜨고 이 undefined와 현재 값을 비교하게 된다. 그럼 서로 다른 값이므로 마지막 값은 무조건 남게 됨.
}

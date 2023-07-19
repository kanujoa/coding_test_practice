// JS에서 Math.min이나 Math.max를 이용해 최소 최대를 구하려면 인자로 배열이 들어갈 수 없으므로 전개 연산자를 써주어야 한다.
function solution(k, score) {
  let result = [];
  let honor = [];
  score.map((s) => {
    if (honor.length < k) honor.push(s);
    else if (Math.min(...honor) < s) {
      honor.splice(honor.indexOf(Math.min(...honor)), 1);
      honor.push(s);
    }
    result.push(Math.min(...honor));
  });
  return result;
}

// 다른 사람의 풀이 (매번 sort, stack의 원리 이용)
function solution(k, score) {
  const stack = []; // 명예의 전당 기록을 위한 배열
  return score.reduce((a, c) => {
    // score를 돌면서 진행
    // a의 초깃값은 빈 배열, 안에 요소를 계속 추가해 나감
    if (stack.length < k) {
      stack.push(c);
      stack.sort((a, b) => a - b);
    } else {
      stack.push(c);
      stack.sort((a, b) => a - b);
      stack.shift(); // 배열에서 첫 번째 요소를 제거하고, 제거된 요소를 반환한다. (여기에서는 가장 작은 요소를 제거 후 반환)
    }
    a.push(stack[0]); // a가 후에 정답으로 반환할 배열로, 현재 stack에서 가장 작은 수(0번째 수)를 넣어주어야 함.
    return a;
  }, []);
}

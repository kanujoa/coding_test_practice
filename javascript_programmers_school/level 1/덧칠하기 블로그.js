function solution(n, m, section) {
  let result = 0;
  while (section.length != 0) {
    const start = section[0];
    for (let i = start; i < start + m; i++) {
      if (section[0] == i) section.shift();
    }
    result += 1;
  }
  return result;
}

// 다른 풀이
function solution(n, m, sections) {
  // m : 벽을 칠하는 롤러의 길이
  var answer = 0; // 정답으로 반환할 최소로 칠하는 횟수
  var painted = 0; // 마지막으로 덧칠해진 구역 번호 (처음에는 덧칠한 부분이 없으므로 0)
  for (var section of sections) {
    // 칠하지 않은 부분(section) 하나씩 순회
    if (painted < section) {
      // 마지막으로 덧칠해진 구역이 현재 section보다 작다면
      answer++; // 덧칠 1회 실시
      painted = section + m - 1; // 마지막으로 덧칠해진 구역은 현재 구역 번호(section)에서 롤러의 길이(m)만큼을 더한 것에서 1을 뺀 것이 됨.
    }
  }
  return answer;
}

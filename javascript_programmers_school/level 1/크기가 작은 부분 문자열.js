function solution(t, p) {
  let answer = 0;
  for (i = 0; i <= t.length - p.length; i++) {
    const slice = t.substr(i, p.length);
    +slice <= +p ? (answer += 1) : null;
  }
  return answer;
}

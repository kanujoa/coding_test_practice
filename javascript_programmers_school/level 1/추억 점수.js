function solution(name, yearning, photo) {
  return photo.map((nameList) => {
    let score = 0;
    nameList.map((n) => {
      if (name.indexOf(n) != -1) score += yearning[name.indexOf(n)];
    });
    return score;
  });
}

// 간단한 풀이
function solution(name, yearning, photo) {
  return photo.map((v) =>
    // yearning 리스트에 name.indexOf(c)의 값이 존재하지 않는 경우(인덱스 초과) 0이 누적됨. (undefined이므로)
    v.reduce((a, c) => (a += yearning[name.indexOf(c)] ?? 0), 0)
  );
}

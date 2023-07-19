function solution(a, b) {
  // 1월 1일이 FRI이므로 아래 계산 결과 나머지가 1이 나오면 FRI라는 뜻
  const dayOfTheWeek = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
  const daysOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  return dayOfTheWeek[
    (daysOfMonth.slice(0, a - 1).reduce((acc, cur) => acc + cur, 0) + b) % 7
  ];
}

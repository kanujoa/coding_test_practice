// sort에 다중 조건이 들어갈 경우 아래와 같이 직접 하나하나 적어주어야 한다.
// 아래는 n번째 문자를 비교한 후 같은 경우에는 문자열 전체를 비교하여 오름차순 정렬을 하는 과정이다.
function solution(strings, n) {
  strings.sort((a, b) => {
    if (a[n] > b[n]) return 1;
    else if (a[n] < b[n]) return -1;
    else {
      if (a > b) return 1;
      else if (a < b) return -1;
      else return 0;
    }
  });
  return strings;
}

// 더 간결한 코드
function solution(strings, n) {
  // strings 배열
  // n 번째 문자열 비교
  return strings.sort((s1, s2) =>
    s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n])
  );
}
// 비교해야 하는 문자인 s1[n]과 s2[n]이 같은 경우 s1과 s2 문자열 전체를 비교해서 오름차순 정렬, 다른 경우 s1[n]과 s2[n](문자열 하나) 비교해서 오름차순 정렬
// localeCompare() 메서드는 참조 문자열이 정렬 순으로 지정된 문자열 앞 혹은 뒤에 오는지 또는 동일한 문자열인지 나타내는 수치를 반환한다.
// 형식 : referenceStr.localeCompare(compareString)
// compareString 전에 referenceStr가 위치하는 경우 음수, compareString 후에 referenceStr가 위치하는 경우 양수, 동등할 경우 0이 됩니다.

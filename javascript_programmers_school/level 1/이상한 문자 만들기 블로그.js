function solution(s) {
  const arr = s.split("");
  let idx = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== " ") {
      idx % 2
        ? (arr[i] = arr[i].toLowerCase()) // JS에서도 인덱스를 통한 값 변경이 가능하다.
        : (arr[i] = arr[i].toUpperCase());
      idx += 1;
    } else idx = 0;
  }
  return arr.join("");
}

// 다른 사람의 풀이
function toWeirdCase(s) {
  return s
    .split(" ")
    .map((i) =>
      i
        .split("")
        .map((j, key) => (key % 2 === 0 ? j.toUpperCase() : j))
        .join("")
    )
    .join(" ");
}

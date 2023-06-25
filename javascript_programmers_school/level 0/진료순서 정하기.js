function criteria(a, b) {
  return b[0] - a[0];
}

function solution(emergency) {
  answer = [];
  for (let i = 0; i < emergency.length; i++) {
    answer.push(0);
  }
  for (let i in emergency) {
    emergency[i] = [emergency[i], Number(i)];
  }
  emergency.sort(criteria);
  for (let i in emergency) {
    answer[emergency[i][1]] = Number(i) + 1;
  }
  return answer;
}

// 다른 사람의 풀이
function solution(emergency) {
  let sort = [...emergency].sort((a, b) => b - a);
  return emergency.map((k) => {
    const queue = sort.findIndex((v) => v === k);

    return queue + 1;
  });
}

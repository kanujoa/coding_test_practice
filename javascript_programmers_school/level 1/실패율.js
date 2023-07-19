function sortStage(a, b) {
  return a - b;
}

function sortFailRate(a, b) {
  if (a[1] > b[1]) return -1;
  else if (a[1] < b[1]) return 1;
  else {
    if (a[0] > b[0]) return 1;
    else if (a[0] < b[0]) return -1;
    else return 0;
  }
}

function solution(N, stages) {
  let failRate = [];
  let people = stages.length;
  stages.sort(sortStage);
  for (let i = 1; i <= N; i++) {
    let fail = 0;
    stages.map((stage) => {
      if (stage == i) fail += 1;
    });
    failRate.push([i, fail / people]);
    people -= fail;
  }
  failRate.sort(sortFailRate);
  return failRate.map((item) => item[0]);
}

function solution(array) {
  const counts = {};     // 숫자와 그의 개수를 담을 객체 counts 생성
  for (let num of array) {     // 인자로 주어진 배열에서의 각각의 원소는 num
      numCount = array.filter(element => element === num).length;     // 각 num을 센 개수는 numCount
      counts[num] = numCount;     // counts의 키는 num, 그의 값은 numCount
  }
  const countsValues = Object.values(counts);     // counts 객체에서 값들(센 개수)만 받아 countsValues 리스트 생성
  let mode = [];     // 최빈값을 담을 리스트 mode 생성 (초깃값은 빈 리스트)
  for (cnt of countsValues) {     // 값들로만 이루어진 리스트에서 값 하나하나는 cnt (array에서 센 개수)
    if (cnt = Math.max(...countsValues)) {     // cnt가 countValues 리스트에서 가장 큰 값일 경우 (가장 많이 세어진 경우)
      mode.push();     // mode 리스트에 그에 해당하는 키를 push (가장 큰 카운트에 해당하는 array의 숫자 (키)를 push)
      console.log(counts[cnt]);

    }
  }
  console.log(mode);
  if (mode.length !== 1) {
    return -1;
  } 
  else  {
    return mode[0];
  }
}

console.log(solution([1, 2, 3, 3, 3, 4, 4]));
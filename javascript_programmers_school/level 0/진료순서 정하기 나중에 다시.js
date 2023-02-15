function solution(emergency) {
  for (i=0; i<emergency.length; i++) {
      let order = 1;
      for (let num of emergency){
        if (emergency[i] < num) {
            order += 1;
        }
      }
    emergency[i] = order;
  }
  return emergency;
}

console.log(solution([3, 76, 24]));
// solution([1, 2, 3, 4, 5, 6, 7]);
// solution([30, 10, 23, 6, 100]);
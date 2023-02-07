function solution(array, height) {
  let result = [];
  for (let i = 0 ; i < array.length; i++) {
      if (array[i] > height) {
          result.push(array[i]);
      }
  }
  return result.length;
}

// 다른 풀이(filter 함수 사용하기)
// function solution(array, height) {
//   var answer = array.filter(item => item > height);
//   return answer.length;
// }


// solution([1,2,3,4],2)
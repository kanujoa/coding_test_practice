function solution(num, total) {
  let result = new Array();
  const middleNum = Math.floor(total / num);
  if (num % 2 !== 0){
    const middleIndex = Math.floor(num / 2);
    result[middleIndex] = middleNum;
    while (result.length < num) {
      for (i = 1; i <= middleIndex; i++) {
        result[middleIndex + i] = middleNum + i;
        result[middleIndex - i] = middleNum - i;
      }
    }
  }
  else {
    const middleIndex = num / 2 - 1; 
    const anotherMiddleIndex = middleIndex + 1;
    result[middleIndex] = middleNum;
    result[anotherMiddleIndex] = middleNum + 1;
    while (result.length < num) {
        for (i = 1; i < anotherMiddleIndex; i++) {     // for문 작성 시 anotherMiddleIndex 부분에 들어가는 수는 1 부분에 들어갈 수보다 커야 한다.
            result[anotherMiddleIndex + i] = middleNum + 1 + i;
            result[middleIndex - i] = middleNum - i;
        }
    }
  }
  return result;
}

console.log(solution(5, 5));
console.log(solution(3, 12));
console.log(solution(5, 15));
console.log(solution(4, 14));

// 간단한 풀이
// function solution(num, total) {
//   var min = Math.ceil(total/num - Math.floor(num/2));     // min은 result에서 가장 작은 값(index가 0인 값)
//   var max = Math.floor(total/num + Math.floor(num/2));     // max는 result에서 가장 큰 값(index가 num-1인 값)

//   return new Array(num).fill(0).map((el,i)=>{return i+min;});     
// }     --> 요소가 num개인 array 객체를 생성 후 0으로 채운 뒤 result에서 가장 작은 값인 min부터 인덱스 번호를 각각 하나씩 더한 값을 요소로 한다.
//           array의 각 요소는 el이 되고 이것을 순회하며 i+min값으로 반환한다.
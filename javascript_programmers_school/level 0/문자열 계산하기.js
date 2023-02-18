function solution(my_string) {
  let split = my_string.split(" ");     // 주어진 입력을 띄어쓰기를 기준으로 나눈 split 리스트 생성
  let result = 0;     // 계산의 결과값이 될 result 변수를 일단 0으로 정의
  while (split.length > 1) {     // split 리스트의 길이가 1보다 클 때까지만 아래의 코드 실행 (최종 결과만 남았을 때 리스트의 길이가 result 값 하나만 담긴 1이 되기 때문!)
    const num1 = parseInt(split[0]);     // 리스트의 왼쪽 부분 3개씩 끊어서 생각
    const num2 = parseInt(split[2]);
    if (split[1] === "+") {
      result = num1 + num2;     // 연산 기호가 +인지 -인지에 따라 계산 결과인 result가 달라짐.
    } else if (split[1] === "-") {
      result = num1 - num2;
    }
    split.splice(0, 3);     // 계산이 끝나면 split 리스트에서 계산이 완료된 3개의 요소들을 제거
    split.splice(0, 0, result);     // split 리스트의 0번 인덱스에 앞의 계산 결과인 result 추가
  }
  return result;     // 최종 계산 결과인 result 반환
}

console.log(solution("3 + 4"));

// 다른 풀이 (eval 사용하지 않고)
// 1 (내가 푼 방법 코드 줄일 수 있는 방법)
// function solution(my_string) {
//   const arr = my_string.split(' ').filter(e=>e);     --> 입력값을 띄어쓰기 기준으로 나누어 리스트에 담고(split(' '))
//   while(arr.length > 1) arr.unshift(+arr.shift() + (arr.shift() === "+" ? 1 : -1) * arr.shift())     --> arr의 길이가 1보다 클 동안만 옆의 코드 실행. 
//   return arr[0]
// }
// * shift 메서드는 배열에서 첫 번째 요소를 제거하고 제거된 요소를 반환한다. shift 메서드는 배열의 길이를 변하게 한다.
// * unshift 메서드는 새로운 요소를 배열의 맨 앞쪽에 추가하고 새로운 길이를 반환한다.
// 두번째 줄 코드에서 arr.shift()를 하여 맨 앞의 숫자를 하나 제거한 뒤 또 한번 더 실행해 제거한 후 그때 반환된 연산 기호가 +이면 1을 arr.shift()를 이용해 세 번째로 반환된
// 숫자에 곱하여 둘을 더하고, -이면 -1을 곱하여 더한다. (뒷 숫자를 양수 또는 음수로 만들어서 더해주는 작업)
// 그리고 한 세트가 끝나면 arr.unshift()로 배열의 맨 앞쪽에 계산 결과를 추가한다.  
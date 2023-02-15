function solution(n) {
  let result = 0;
  for (i = 1; i <= n; i++) {
      if (n % i === 0){
          result += 1;
      }
  }
  return result;
}

// 다른 풀이 
function solution(n) {
  return Array(n).fill(1).map((v,idx) => v + idx).filter(v => n % v === 0).length     
}     // fill(1)로 길이가 n인 배열의 처음부터 끝까지 1로 채우고 배열의 각 요소에 각 인덱스 숫자를 더해 1부터 n까지의 숫자가 들어있는 리스트를 만든다.
// 그 후 filter로 n과 각 배열의 요소들을 나누어 나머지가 0이 되는 배열의 요소들만 리스트에 남기고 그 길이를 구하면 답이다.
// 답은 결국 n의 약수의 개수가 되기 때문이다.

console.log(Array(3));     // empty x 3의 배열 객체가 만들어짐.
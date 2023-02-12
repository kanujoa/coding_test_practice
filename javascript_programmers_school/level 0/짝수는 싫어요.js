function solution(n) {
  const newArr = [];
  for (let num = 1; num <= n; num ++) {
      if (num % 2 === 1) {
          newArr.push(num);
      }
  }
  return newArr.sort((a, b) => a - b);      // 어차피 for문에서 num이 1부터 증가하도록 설정해 주었으므로 newArr은 자동으로 오름차순 리스트가 된다. 따라서 옆의 것은 안 써주어도 됨.
}

// 다른 풀이 1
// function solution(n) {
//   var answer = [];
//   for (let i = 1; i<=n; i+=2) answer.push(i)     --> i+=2를 써주면 %를 하지 않아도 홀수만 골라낼 수 있다.     
//   return answer;
// }

// 다른 풀이 2
// function solution(n) {
//   return Array(n).fill(1).map((v,i)=>v+i).filter(v=>v%2===1);     
// }
// --> n개의 길이만큼의 배열(Array(n))을 1로만 채움.(.fill(1)) 그 후 map 메서드로 1(v)과 각 index(i)를 더해주어 1부터 요소의 개수인 n까지를 각 요소로 가지는 리스트를 반환
// 그리고 filter로 그 리스트를 순회하면서 2로 나눈 나머지가 1인 요소들로만 이루어진 리스트를 반환

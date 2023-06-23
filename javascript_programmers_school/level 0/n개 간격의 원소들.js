function solution(num_list, n) {
  let answer = [];
  for (let i = 0; i < num_list.length; i += n) {
    // i의 값을 변화시킬 때는 i + n이 아닌 i += n으로 적어주어야 함.
    answer.push(num_list[i]);
  }
  return answer;
}

// 다른 풀이 (_는 사용하지 않을 변수라는 의미)
const solution = (arr, d) => arr.filter((_, idx) => idx % d === 0); // 현재 idx가 주어진 간격으로 나누었을 때 나머지가 0이라면 해당 요소는 포함되어야 함.

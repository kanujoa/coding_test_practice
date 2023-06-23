function solution(num_str) {
  const answer = num_str.split("").reduce((acc, cur) => acc + Number(cur), 0);
  return answer;
} // 초깃값 0을 설정해주지 않으면 초깃값이 문자가 되어 문자열 + 숫자 의 연산이 되기 때문에 일반적인 경우와 다르게 초깃값 0을 넣어 주어야 함.

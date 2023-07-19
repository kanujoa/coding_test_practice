function solution(nums) {
  const set = new Set(nums);
  if ([...set].length < nums.length / 2) return [...set].length;
  else return nums.length / 2;
}
// JS에서 set.length로 집합의 길이를 구할 수 없으므로 전개 연산자를 통해 배열로 바꾸어 주었다.

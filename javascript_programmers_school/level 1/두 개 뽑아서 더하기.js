function solution(numbers) {
  const nums = new Set();
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) nums.add(numbers[i] + numbers[j]);
    }
  }
  return Array.from(nums).sort((a, b) => a - b);
}
// Array.from(nums) 대신 [...nums]를 사용해도 된다.

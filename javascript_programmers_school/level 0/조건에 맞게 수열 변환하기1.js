function solution(arr) {
  return arr.map((item) => {
    if (item >= 50 && item % 2 === 0) {
      return item / 2;
    } else if (item < 50 && item % 2 === 1) {
      return item * 2;
    } else {
      return item;
    }
  });
}
// map 메서드에 들어갈 함수를 작성하고 반환할 값은 항상 return과 함께 적어주어야 함.

// 다른 풀이
function solution(arr) {
  return arr.map((num) => {
    if (num >= 50 && !(num % 2)) return num / 2; // 이렇게 !를 써주면 not의 의미가 됨. (num % 2 가 1일 아닐 때 참이 된다는 뜻)
    if (num < 50 && num % 2) return num * 2;
    return num;
  });
}

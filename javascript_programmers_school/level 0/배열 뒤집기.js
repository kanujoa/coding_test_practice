// 방법 1. reversed 메서드 사용하여 구현하기
function solution(num_list) {
  num_list.reverse();
  return num_list;
}

// 방법 2. result 리스트를 따로 만들어 num_list의 요소들을 뒤에서부터 push하기 (reverse 메서드 사용하지 않고 구현하기)
function solution(num_list) {
  result = [];
  for (i = num_list.length - 1; i >= 0; i--) {
      result.push(num_list[i]);
  }
  return result;
}

// 방법 3. num_list 안에서 수를 옮겨 해결하기
function solution(num_list) {
  const len = num_list.length;     // 작성하기 편하게 len 변수 생성
  for (i = 0; i < len; i++) {
      num_list.splice(i, 0, num_list[len - 1]);     // num_list의 i번 인덱스에 num_list의 마지막 요소가 추가되게 함.
      num_list.splice(len, 1);     // num_list의 마지막 요소를 삭제함.
  }
  return num_list;
}
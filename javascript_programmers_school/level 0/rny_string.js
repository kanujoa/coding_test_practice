function solution(rny_string) {
  rny_string = rny_string.replace(/m/g, "rn"); // 정규식 사용하기
  return rny_string;
}
// 1. js에서 내가 원하는 문자로 모두 치환하기
// 정규식으로 찾으려는 문자열은 '/'으로 감싸서 파라미터로 들어가는 값이 정규식임을 알려준다.
// 그리고 '/' 뒤에는 g(global match)라는 modifier를 붙여준다.

// 2. 대소문자 구분 없이 모두 치환하기
// g modifier와 함께 i modifier도 함께 적어주면 된다.

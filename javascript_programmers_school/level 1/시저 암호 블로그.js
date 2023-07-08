function solution(s, n) {
  return s
    .split("")
    .map((item) => {
      if (item != " ") {
        let push = +item.charCodeAt() + n; // JS에서 문자를 아스키 코드에서의 10진 숫자로 변경하는 메서드 : string.charCodeAt()
        if (item === item.toUpperCase())
          // JS에서는 대문자인지 확인하는 메서드가 없으므로 item과 item을 대문자로 변환한 것이 같을 경우 item이 대문자가 맞는 것으로 간주하였다.
          return String.fromCodePoint(
            65 + ((push - 65) % 26)
          ); // JS에서 아스키 코드 10진 숫자를 문자로 변경하는 메서드 : string.fromCodePoint()
        else return String.fromCodePoint(97 + ((push - 97) % 26));
      } else return item;
    })
    .join("");
}

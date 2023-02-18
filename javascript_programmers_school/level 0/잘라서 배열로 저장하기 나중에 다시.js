function solution(my_str, n) {
  let str = my_str;
  const result = [];
  for (i = 1; i <= Math.ceil(my_str.length / n); i++) {
    if (str.length < Math.ceil(my_str.length / n)) {
      result.push(str);
    } else {
      const cut = str.substr(0, n);
      result.push(cut);
      str = str.replace(cut, "");
    }
  }
  return result;
}

console.log(solution("abc1Addfggg4556b", 6));
console.log(solution("abcdef123", 3))
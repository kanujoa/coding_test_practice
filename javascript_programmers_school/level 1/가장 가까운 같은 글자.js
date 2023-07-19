function solution(s) {
  let result = [];
  let location = {};

  for (let i = 0; i < s.length; i++) {
    if (Object.keys(location).includes(s[i])) {
      result.push(i - location[s[i]]);
      location[s[i]] = i;
    } else {
      result.push(-1);
      location[s[i]] = i;
    }
  }

  return result;
}

// 비슷하지만 더 간단하게 작성하기
function solution(s) {
  const hash = {};

  return [...s].map((v, i) => {
    let result = hash[v] !== undefined ? i - hash[v] : -1;
    hash[v] = i;
    return result;
  });
}

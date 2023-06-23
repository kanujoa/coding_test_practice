function solution(my_string, index_list) {
  answer = [];
  for (i of index_list) {
    answer.push(my_string[i]);
  }
  return answer.join("");
}
// js에서는 python에서와 다르게 ''.join(list) 형태가 아닌 array.join('')의 형태로 작성하여야 한다.

// 다른 사람의 풀이 (map 사용)
function solution(my_string, index_list) {
  return index_list.map((i) => my_string[i]).join("");
}
// map의 인자로 들어가는 함수의 인자는 차례로 item, index, array임. 지금은 하나만 적어주었으므로 item에 해당
// index_list의 item을 하나씩 돌면서 my_string[i]로 대체된 것이 배열로 반환됨.
// 마지막에는 반환된 배열을 join으로 묶어주면 끝

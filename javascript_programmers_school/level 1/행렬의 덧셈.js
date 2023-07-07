function solution(arr1, arr2) {
  let answer = [];
  for (i in arr1) {
    let tmp = [];
    for (j in arr1[i]) {
      tmp.push(arr1[i][j] + arr2[i][j]);
    }
    answer.push(tmp);
  }
  return answer;
}

// 다른 사람의 풀이 (map 이용, A는 arr1, B는 arr2라고 생각하면 됨.)
function solution(A, B) {
  return A.map((arr1, idx1) => arr1.map((val, idx2) => val + B[idx1][idx2]));
}
// arr1의 값을 B의 똑같은 인덱스의 값을 더한 값으로 업데이트하는 식으로 진행

function bin(num) {
  let binary = [];
  while (num != 0) {
    binary.push(num % 2);
    num = Math.floor(num / 2);
  }
  return binary.reverse().join("");
}

function solution(n, arr1, arr2) {
  let answer = [];
  for (let i = 0; i < n; i++) {
    const map_1 = "0".repeat(n - bin(arr1[i]).length) + bin(arr1[i]);
    const map_2 = "0".repeat(n - bin(arr2[i]).length) + bin(arr2[i]);
    let tmp = [];
    for (let j = 0; j < n; j++) {
      if (map_1[j] == 0 && map_2[j] == 0) tmp.push(" ");
      else tmp.push("#");
    }
    answer.push(tmp.join(""));
  }
  return answer;
}

// 다른 사람의 풀이
function solution(n, arr1, arr2) {
  let num1, num2, s;
  let answer = [];
  //manually turning decimals to binaries cos i can!
  for (let i = 0; i < n; i++) {
    num1 = arr1[i];
    num2 = arr2[i];
    s = "";
    for (let j = 0; j < n; j++) {
      s = (num1 % 2) + (num2 % 2) ? "#" + s : " " + s;
      num1 = Math.floor(num1 / 2);
      num2 = Math.floor(num2 / 2);
    }
    answer.push(s);
  }
  return answer;
}

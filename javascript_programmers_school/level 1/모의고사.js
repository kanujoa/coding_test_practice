function scoring(student, answers, idx) {
  // 인덱스 설정 주의하기 (idx는 0부터 시작하므로 %할 때 student배열의 길이로 해야 함. +1을 하면 안됨!)
  if (student[idx % student.length] == answers[idx]) return true;
  else return false;
}

function solution(answers) {
  let result = [];
  const first = [1, 2, 3, 4, 5];
  const second = [2, 1, 2, 3, 2, 4, 2, 5];
  const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let f_score = 0,
    s_score = 0,
    t_score = 0;
  for (let i = 0; i < answers.length; i++) {
    if (scoring(first, answers, i)) f_score += 1;
    if (scoring(second, answers, i)) s_score += 1;
    if (scoring(third, answers, i)) t_score += 1;
  }
  const max_score = Math.max(f_score, s_score, t_score);
  if (f_score == max_score) result.push(1);
  if (s_score == max_score) result.push(2);
  if (t_score == max_score) result.push(3);
  return result;
}

// 조금 더 깔끔하게 작성하기 (forEach 사용!)
function solution(answers) {
  const answer = [];
  let person1 = 0,
    person2 = 0,
    person3 = 0;
  const pick1 = [1, 2, 3, 4, 5],
    pick2 = [2, 1, 2, 3, 2, 4, 2, 5],
    pick3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  answers.forEach((answer, idx) => {
    if (pick1[idx % pick1.length] === answer) person1++;
    if (pick2[idx % pick2.length] === answer) person2++;
    if (pick3[idx % pick3.length] === answer) person3++;
  });

  const maxAnswer = Math.max(person1, person2, person3);

  if (person1 === maxAnswer) answer.push(1);
  if (person2 === maxAnswer) answer.push(2);
  if (person3 === maxAnswer) answer.push(3);
  return answer;
}

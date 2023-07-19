function solution(array, commands) {
  return commands.map((item) => {
    const cut = array.slice(item[0] - 1, item[1]);
    cut.sort((a, b) => a - b);
    return cut[item[2] - 1];
  });
}

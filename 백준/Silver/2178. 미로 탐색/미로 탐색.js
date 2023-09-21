let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 칸을 옮기기 위한 좌표
const ds = [
  [-1, 0],
  [1, 0],
  [0, 1],
  [0, -1],
];
// 목적지 x좌표(N)와 y좌표(M)
const [N, M] = input.shift().split(" ").map(Number);
// 방문한 곳까지의 거리를 저장하기 위해 주어진 N과 M을 가지고 같은 크기의 2차원 배열을 만들어 줌.
const visit = [...Array(N)].map((e) => Array(M).fill(0));
// graph는 문제에서 주어지는 미로
const graph = [];
for (let i = 0; i < N; i++) {
  graph.push([...input[i].replace(/\r/g, "").split("").map(Number)]);
}

// bfs에 활용할 큐 선언, 처음 값으로는 탐색 시작 부분인 [0, 0]이 들어 있음.
const queue = [[0, 0]];
// (0, 0)에 1 기록 (거리는 1부터 시작)
visit[0][0] = 1;
// queue가 다 비워지기 전까지 아래 코드 반복
while (queue.length) {
  // queue에 있는 첫번째 값을 꺼내어 x좌표, y좌표 구조 분해 할당
  const [x, y] = queue.shift();
  // graph[x][y]가 0인 경우 queue의 다음 요소로 (아래 코드는 건너뛰기)
  if (!graph[x][y]) continue;
  graph[x][y] = 0; // graph[x][y]가 1인 경우 방문 처리

  // 상하좌우를 다 살피기 위해 4번 for문 돌기
  for (let i = 0; i < 4; i++) {
    // 새로운 x의 위치와 y의 위치 지정하기 (상 또는 하 또는 좌 또는 우 방향으로 1칸만 움직일 수 있다.)
    const xPos = x + ds[i][0];
    const yPos = y + ds[i][1];

    // 새로운 x 위치와 y 위치가 0보다 작으면 불가하므로 continue, 또는 최대인 N, M보다 값이 커도 불가하므로 continue
    if (xPos < 0 || yPos < 0 || xPos >= N || yPos >= M) continue;
    // 만약 새로운 x, y 위치에 있는 수가 1이라면
    if (graph[xPos][yPos]) {
      // 그 위치에서 주변을 살펴야 하므로 queue에 그 위치를 push
      queue.push([xPos, yPos]);
      // 처음 위치에서 그 위치까지의 거리를 기록 (현재 위치에서 한칸 움직이므로 +1만 하면 됨.)
      visit[xPos][yPos] = visit[x][y] + 1;
    }
  }
}

// 최종 목적지 위치에 기록된 거리 값을 출력하면 됨.
console.log(visit[N - 1][M - 1]);
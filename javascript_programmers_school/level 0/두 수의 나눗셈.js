const solution = (num1, num2) => Math.floor(num1 / num2 * 1000)

// Math.floor 메서드
// Math.floor(3.5) = 3
// Math.floor(3.87) = 3
// Math.floor(-3.5) = -4     --> 더 작은 정수 중 입력값과 가장 가까운 정수
// Math.floor(-3.14) = -4

// Math.turnc 메서드
// Math.turnc(3.5) = 3
// Math.turnc(3.87) = 3
// Math.turnc(-3.5) = -3     --> 그냥 소수점 아래만 삭제
// Math.turnc(-3.14) = -3
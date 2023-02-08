const solution = (num1, num2) => parseInt(num1 / num2);     // js에서는 python에서 사용하는 // 사용 불가

//큰 수에서는 type number에 string이 들어가는 경우도 있기 때문에, 소수점 이하를 절삭하여 정수 값을 return하려는 목적으로 Math.floor 대신에 parseInt 사용 불가
// const solution = (num1, num2) => Math.floor(num1 / num2);      이렇게 풀기!
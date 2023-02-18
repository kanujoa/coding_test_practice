// function solution(A, B) {
//   const split = A.split("");
//   if (A === B) {
//     return 0;
//   }
//   else {
//     var count = 0;
//     while (A === B) {
//       for (i = 0; i < A.length; i++) {
//         if (i !== A.length - 1) {
//           A[i+1] = split[i];
//         } 
//         else {
//           A[0] = split[i];
//         }
//       }
//       count += 1;
//       if (count >= A.length) {
//         return -1
//       }
//     }
//     return count;
//   }
// }

const A = "hello";
const split = A.split("");

for (i = 0; i < A.length; i++) {
  var rightPush;
  if (i != A.length - 1) {
    rightPush = A.replace(A[i+1], split[i]);
  } 
  else {
    rightPush = A.replace(A[0], split[i]);
  }
}

console.log(rightPush);
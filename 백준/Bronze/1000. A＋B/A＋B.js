const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

let [ A, B ] = input.map(num => Number(num))
console.log( A + B );
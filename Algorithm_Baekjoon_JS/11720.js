const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const nums = input[1].split('').map(Number);
const result = nums.reduce((acc, cur) => acc + cur, 0);
console.log(result);

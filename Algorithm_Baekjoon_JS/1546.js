const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const n = Number(input[0]);
const nums = input[1].split(' ').map(Number);
const maxNum = Math.max(...nums);
const hap = nums.reduce((acc, num) => {
  acc += (num / maxNum) * 100;
  return acc;
}, 0);
const result = hap / n;
console.log(result % parseInt(result) === 0 ? result.toFixed(1) : result);

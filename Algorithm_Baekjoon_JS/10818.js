const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const nums = input[1].split(' ').map(Number);
const numMax = Math.max(...nums);
const numMin = Math.min(...nums);
console.log(`${numMax} ${numMin}`);

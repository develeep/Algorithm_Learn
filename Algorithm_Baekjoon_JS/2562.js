const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const numInput = input.map(Number);
const max = Math.max(...numInput);
const maxIndex = numInput.findIndex((n) => n === max);
console.log(max);
console.log(maxIndex + 1);

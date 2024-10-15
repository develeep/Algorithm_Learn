const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

input.shift();

input.sort((a, b) => a - b);
console.log(input.join('\n'));

const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');
const a = +input[0];
const b = +input[1];
console.log(a + b);

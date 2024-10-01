const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const str = [...input[0]];
const num = +input[1] - 1;
console.log(str[num]);

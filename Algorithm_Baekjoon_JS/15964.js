const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split(' ');

const [a, b] = input.map((n) => +n);
const result = (a + b) * (a - b);
console.log(result);

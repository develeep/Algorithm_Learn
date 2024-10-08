const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const result = new Set(input.map((n) => n % 42));
console.log(result.size);

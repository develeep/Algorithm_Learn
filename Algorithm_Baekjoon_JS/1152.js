const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split(' ');

const strs = input.filter((str) => str !== '');
console.log(strs.length);

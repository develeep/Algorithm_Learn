const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split(' ');

const result =
  input.reduce((hap, num) => {
    return hap + Math.pow(+num, 2);
  }, 0) % 10;

console.log(result);

const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

input.shift();

input.sort((a, b) => {
  if (a.length === b.length) {
    if (a < b) return -1;
    else if (a > b) return 1;
    else return 0;
  } else {
    return a.length - b.length;
  }
});
const strs = new Set(input);
console.log([...strs].join('\n'));

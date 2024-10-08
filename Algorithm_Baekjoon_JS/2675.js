const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

input.slice(1, input.length).forEach((n) => {
  const [r, str] = n.split(' ');
  const p = str.split('').reduce((acc, cur) => {
    return (acc += cur.repeat(r));
  }, '');
  console.log(p);
});

const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const mulNum = input.reduce((acc, num) => {
  return acc * Number(num);
}, 1);

const result = mulNum
  .toString()
  .split('')
  .reduce(
    (acc, n) => {
      acc[n] += 1;
      return acc;
    },
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  );

result.forEach((n) => {
  console.log(n);
});

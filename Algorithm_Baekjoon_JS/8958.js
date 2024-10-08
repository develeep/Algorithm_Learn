const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

input.splice(1, input.length).forEach((str) => {
  const res = str.split('').reduce(
    (acc, cur) => {
      acc[1] += cur === 'O' ? ++acc[0] : (acc[0] = 0);
      return acc;
    },
    [0, 0]
  );
  console.log(res[1]);
});

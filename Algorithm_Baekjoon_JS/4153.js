const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

input.pop();
input.forEach((triangle) => {
  const [a, b, c] = triangle.split(' ').map((n) => +n * +n);

  if (a + b === c || a + c === b || b + c === a) {
    console.log('right');
  } else {
    console.log('wrong');
  }
});

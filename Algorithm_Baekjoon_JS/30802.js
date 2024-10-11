const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const N = Number(input[0]);
const shirts = input[1].split(' ').map(Number);
const [T, P] = input[2].split(' ');
const pens = [Math.floor(N / P), N % P];
const shirt = shirts.reduce((acc, cur) => {
  acc += Math.ceil(cur / T);
  return acc;
}, 0);
console.log(shirt);
console.log(`${pens[0]} ${pens[1]}`);

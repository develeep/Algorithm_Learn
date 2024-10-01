const input = require('fs').readFileSync(0, 'utf-8').toString().trim();

const n = [...input];

const x = {
  A: 4,
  B: 3,
  C: 2,
  D: 1,
  F: 0,
};
const y = {
  '+': 0.3,
  0: 0,
  '-': -0.3,
};
const result = x[n[0]] + (n[1] ? y[n[1]] : 0);
console.log(result.toFixed(1));

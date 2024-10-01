const input = require('fs').readFileSync(0, 'utf-8').toString().trim();
const arr = [...input].map((str) =>
  str.toLowerCase() === str ? str.toUpperCase() : str.toLowerCase()
);
console.log(arr.join(''));

const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map(Number);
const cards = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);

let result = 0;
for (i = n - 1; i >= 0; i--) {
  for (j = i - 1; j >= 0; j--) {
    for (k = j - 1; k >= 0; k--) {
      const cardSum = cards[i] + cards[j] + cards[k];
      if (cardSum === m) {
        result = cardSum;
        // break;
      } else if (cardSum <= m && cardSum > result) {
        result = cardSum;
      }
    }
    if (result === m) {
      break;
    }
  }
  if (result === m) {
    break;
  }
}
console.log(result);

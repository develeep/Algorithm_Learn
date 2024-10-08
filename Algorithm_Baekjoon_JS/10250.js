const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

input.slice(1, input.length).forEach((line) => {
  const [h, w, n] = line.split(' ').map(Number);
  const room = n % h === 0 ? parseInt(n / h) : parseInt(n / h) + 1;
  const floor = n % h === 0 ? h : n % h;
  console.log(`${floor}${room < 10 ? '0' + room : room}`);
});

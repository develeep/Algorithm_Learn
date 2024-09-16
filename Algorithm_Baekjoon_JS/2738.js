// 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
// 1 초	128 MB	98124	51593	44715	53.078%
// 문제
// N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

// 출력
// 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
const input = require('fs')
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map((i) => +i);
input.shift();

// const arr = input.reduce((acc, cur, idx) => {
//   if (idx < n) {
//     acc['a'] = acc['a'] ? [...acc['a'], ...cur.split(' ')] : cur.split(' ');
//   }
//   if (idx >= n) {
//     acc['b'] = acc['b'] ? [...acc['b'], ...cur.split(' ')] : cur.split(' ');
//   }
//   return acc;
// }, {});

// const result = arr.a.reduce((acc, cur, idx) => {
//   return [...acc, +cur + +arr.b[idx]];
// }, []);

// for (i = 0; i < n; i++) {
//   const spliceArr = result.splice(0, m);
//   console.log(spliceArr.join(' '));
// }

// 일케 간단히도 할수 있구나..
for (i = 0; i < n; i++) {
  const a = input[i].split(' ').map((x) => +x);
  const b = input[i + n].split(' ').map((x) => +x);
  console.log(a.map((num, idx) => num + b[idx]).join(' '));
}

// 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
// 1 초	256 MB	177246	97455	80340	55.218%
// 문제
// 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

// 출력
// 첫째 줄에 N!을 출력한다.
const input = require('fs').readFileSync('./dev/stdin').toString().trim();

//for문 이용
// let result = 1;
// for (i = 1; i <= input; i++) {
//   result *= i;
// }
// console.log(result);

// 재귀함수 이용
function pac(num) {
  if (num < 1) return 1;
  return num * pac(num - 1);
}
console.log(pac(+input));

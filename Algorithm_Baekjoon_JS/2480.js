// 문제
// 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

// 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
// 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
// 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
// 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

// 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

// 입력
// 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

// 출력
// 첫째 줄에 게임의 상금을 출력 한다.

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

//1번 방법 (난잡)
// const first = input[0] === input[1];
// const second = input[0] === input[2];
// const third = input[1] === input[2];
// const fourth = first & third;
// const max = Math.max(...input.map((a) => +a));
// const result = fourth
//   ? 10000 + input[0] * 1000
//   : first | second
//   ? 1000 + input[0] * 100
//   : third
//   ? 1000 + input[2] * 100
//   : max * 100;
// console.log(result);

//2번방법 (더 간단)
const dict = input.reduce((acc, input) => {
  acc[input] = acc[input] ? acc[input] + 1 : 1;
  return acc;
}, {});
let result = 0;
Object.entries(dict).forEach(([key, value]) => {
  if (value === 3) {
    result = 10000 + key * 1000;
  } else if (value === 2) {
    result = 1000 + key * 100;
  }
});
console.log(result ? result : Math.max(...input.map((a) => +a)) * 100);

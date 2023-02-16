/*
 *
 * 아래 예시 코드에는 5번의 콘솔 출력문이 반복되고 있습니다.
 * 우리는 이 코드를 개선해보도록 하겠습니다.
 *
 * 5개의 원소를 가진 배열이 주어졌다고 가정했을때,
 * 해당 배열의 원소들을 순서대로 콘솔 출력하는 로직을 작성해보시는 것이 미션입니다.
 *
 */
const list = [1, 2, 3, 4, 5];

// [예시] 반복문을 활용하지 않은 코드입니다.
console.log(list[0]);
console.log(list[1]);
console.log(list[2]);
console.log(list[3]);
console.log(list[4]);

// [미션] 위 예시와 결과적으로 동일한 로직을 수행하도록 아래에 여러분의 코드를 작성해주세요.
// (켄: 첫 번째 챌린지는 예시 삼아, 제가 미리 완성해놓았습니다.)
for (let i = 0; i < 5; i++) {
  console.log(list[i]);
}
// 12
/**
 * @param {number[]} height
 * @return {number}
 */

var trap = function (height) {
  let i = 0;
  amt = 0;
  while (i < height.length) {
    if (
      height[i] === Math.min(...height) ||
      (uniqueMax(height) &&
        height[i] === Math.max(...height) &&
        !uniqueMax(height.slice(i + 1)))
    ) {
      i += 1;
      continue;
    }
    const nextIndex = nextVal(i, height, uniqueMax);
    if (nextIndex === -1) break;
    amt +=
      height[i] * Math.abs(i + 1 - nextIndex) -
      sumArray(height.slice(i + 1, nextIndex));
    i = nextIndex;
  }
  return amt;
};

function nextVal(currIndex, arr, uniqueMax) {
  for (let i = currIndex + 1; i < arr.length; i++) {
    if (uniqueMax && arr[currIndex] === Math.max(...arr)) {
      
    } else if (arr[i] >= arr[currIndex]) {
      return i;
    }
  }
  return -1;
}

function sumArray(arr) {
  return arr.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    0
  );
}

function uniqueMax(arr) {
  return arr.filter((x) => x == Math.max(...arr)).length === 1;
}

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));

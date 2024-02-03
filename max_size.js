//https://leetcode.com/problems/container-with-most-water/description/

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let maxArea = 0;
  
  const heightData = height.map((height, index) => ({
    height,
    index,  
  }));
  for (let i = 0; i < heightData.length; i++) {
    if (
      heightData[i].height *
      Math.max(
        Math.abs(heightData[i].index - 0),
        Math.abs(heightData[i].index - (height.length - 1))
      ) < maxArea
    )
      continue;
    const availableHeights = heightData.filter(
      (x) => x.height >= heightData[i].height && x.index !== heightData[i].index
    );

    if (availableHeights.length < 1) continue;

    const extremes = extremeValues(availableHeights);
    const newArea =
      heightData[i].height *
      Math.max(
        Math.abs(heightData[i].index - extremes[0]),
        Math.abs(heightData[i].index - extremes[1])
      );

    if (newArea > maxArea) {
      maxArea = newArea;
    }
  }
  return maxArea;
};

function extremeValues(data) {
  const values = data.map((x) => x.index);
  return [Math.min(...values), Math.max(...values)];
}
// console.log(

// );

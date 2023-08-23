function solution(nums) {
    // let numCnt = {};
    // for (let num of nums) {
    //     if (Object.keys(numCnt).includes(+num)) numCnt[num] += 1;
    //     else numCnt[num] = 1;
    // }
    const set = new Set(nums);
    if ([...set].length < nums.length / 2) return [...set].length;
    else return nums.length / 2;
}
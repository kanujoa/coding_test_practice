function solution(arr) {
    const stack = [];
    
    for (let num of arr) {
        if (stack[stack.length - 1] !== num) stack.push(num); 
    }
    
    return stack;
}
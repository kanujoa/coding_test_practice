function solution(participant, completion) {
    const hashTable = {};
    
    for (let person of participant) {
        if (!hashTable[person]) hashTable[person] = 1;
        else hashTable[person] += 1;
    }
    
    for (let person of completion) {
        hashTable[person] -= 1;
        if (hashTable[person] === 0) delete hashTable[person];
    }
    
    return Object.keys(hashTable)[0];
}
function palindromePermutation(str){
    let charCount = new Set();
    str = str.toLowerCase().replace(/[^a-z]/g, '');

    for(let i = 0; i < str.length; i++){
        let char = str.charAt(i); //loop through each char and store it in var c
        
        if (charCount.has(char)){
            charCount.delete(char);
        }
        else{
            charCount.add(char);
        }
    }
    return charCount.size <= 1;
}

//must have a match for every character except for one. keep track of everything in a hash
// if string even length, char must have even count
//if string odd, every character except 1 should have even count

console.log(palindromePermutation("Tact Coa")) //true
console.log(palindromePermutation('bba'))   //true
console.log(palindromePermutation("super")) //false
console.log(palindromePermutation("ra ce rac")) //true

// Return the number of vowel  in a string

function vowelCountInString(strr){
    const vl = ['a','i','e','o','u'];
    var count = 0;
    for(let i=0; i<strr.length; i++){
        if((vl.includes(strr[i])) === true){
            count += 1;
        }
    } return count 
}
const a = 'WASILAT';
console.log(vowelCountInString(a.toLowerCase()));
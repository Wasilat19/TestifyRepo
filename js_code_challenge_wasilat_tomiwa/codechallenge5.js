// // No 5: Create a Function that reverses an array

function reverseArray(a){
    var b = [];
    for(let i=a.length-1; i>=0; i--){
         b.push(a[i])                   
        } 
    return b;      
 }

 c = ['Jonah','Tomiwa','Henry','Wasilat','Tomiwa', 5, 8, 0]
 console.log(reverseArray(c))


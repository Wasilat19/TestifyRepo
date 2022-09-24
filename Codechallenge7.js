//Sort an Array of Numbers in descending Order


function sortArrayNumDesc(numArray) {
    let num = numArray.sort((a, b)=> b - a)
    return num
}
console.log(sortArrayNumDesc([100, 50, 10, 3, 10, 6, 8, 2, 200]))


//Create a function that filters out negative numbers

function filterNegativeNumbers(array) {
    return array.filter(function (num){
    return num > 0
    })
}
console.log(filterNegativeNumbers([-4,-5,-8,10,45,66,-90,-45,33]))
// Create a Length converter function

// This function converts inches to centimeters and vice versa
// conversion rate: 1 inch = 2.54cm
function inchCentimeter(a){
    const cm = a * 2.54
    const inch = a/2.54
    return [{cm,a}, {a,inch}]
}
console.log(inchCentimeter(10))

// This function converts cm to m
// conversion rate: 1cm = 0.01m
function cmm(a) {
    const m = a * 0.01
    const cm = a/0.01
    return[{m,a}, {a,cm}]
}
console.log(cmm(10))

// This function converts ft to inches
// conversion rate: 12 inches = 1 foot
function ftinch(a){
    const inch = a * 12
    const ft = a/12
    return[{inch,a}, {a,ft}]
}
console.log(ftinch(10))



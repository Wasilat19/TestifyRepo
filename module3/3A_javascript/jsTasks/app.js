// Lesson13  Strings Concatenation

// const age = 20
// const name = 'Wasilat'
// const sentence = 'My name is '+ name +'. '+'I am '+age+' years old.'

// console.log(sentence)

// Lesson 14 (data types)

// const isBritish = true
// const isNight = false

// const userDetails = null

// console.log(typeof(isBritish))



// Comparison Operators
// const compare = 4 > 3

// console.log(compare)


// Lesson 17 (logical operators)
// AND ---> && all must be true
// OR ---> || either must be true
// NOT --- ! toggle boolean values

// const userName = 'Victory'
// const age = 12

// const logic = age ===12 && userName === 'Victory'

// console.log(logic)


// Lesson 18 (Conditional statements 'if', 'if else')

// const age = 15

// if(age>=18){
//     console.log('You are eligible to vote')
// } else {
//     console.log('You are too young to vote')
// }
// const age = 78

// if(age>=18 && age<= 65){
//     console.log('You are eligible to vote')
// } else if(age>65) {
//     console.log('You are too old to vote')
// } else { 
//     console.log('You are too young to vote')
// }



// Lesson 20 (Switch statement)

const day = 'Saturday'

// if(day==='Friday') {
//     console.log('TGIF!')
// } else if(day==='Saturday') {
//     console.log('Yeh! The weekend is here')
// }else if(day==='Sunday') {
//     console.log('Happy Sunday!')
// } else { 
//     console.log('Go to work!')
// }


// switch(day){
//     case 'Friday':
//         console.log('TGIF!')
//         break
//     case 'Saturday':
//         console.log('Yeh! The weekend is here')
//         break
//     case 'Sunday':
//         console.log('Happy Sunday!')
//     default:
//         console.log('Go to work!')   
// }

// lesson 21 (while loops)
// let star = 1
// while(star <=100 ) {
//     if (star===1) { 
//         console.log(star +' star')    
//     }else{ 
//         console.log(star +' stars')
//     }
//     star = star + 1
// }

// lesson 22 (for-loops)
// for(star=0; star<=10; star=star+1) { 
//     if(star===1 || star===0) { 
//         console.log(star +' star')
//     } else {
//         console.log(star + ' stars')
//     }
// }

// lesson 23 (FUNCTIONS)
// function greeting(name) {
//     console.log('Good morning, ' + name)
// }

// greeting('Wasilat')

// function addNumbers (firstNumber,secondNumber) {
//     const sum = firstNumber + secondNumber
//     console.log(sum)
// }

// addNumbers(20, 20)


// Lesson 24 (Return values)
// function addNumbers (firstNumber,secondNumber) {
//         const sum = firstNumber + secondNumber
//         const product = firstNumber * secondNumber
//         return [sum, product]
//     }
//     console.log(addNumbers(4,5))


// function converter(dollar) {
//     // convert to naira and return the equivalent naira value
//     // convertion rate: 410 naira to 1 dollar
//     const naira = dollar * 410
//     return naira
// }
// const nairaValue = converter(100)

// console.log(nairaValue)

// function converter(length) {
//     // convert inch to cm and return the cm value
//     // convertion rate: 2.54cm to 1 inch
//     const cm = length * 2.54
//     const inch = length/2.54
//     return [cm, inch]
// }
// const inchCm = converter(10)
// console.log(inchCm)

// Lesson 26 Function expression

// function greet(name) {
//     console.log('Good morning, ' + name)
// }
// // This is an declared function because you can call it from anywhwere within your code
// greet("Nick")

const myGreet = function(name) {
    console.log("Good morning," + name)
}
myGreet("Nick")  
// This is an expressed function

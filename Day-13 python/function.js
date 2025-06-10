// function daa()
// {
//     console.log("hai")
// } daa()

// function greet(name)
// {
//     console.log("hello",name)
// } greet("sailu")


// anonymous functions.....

// const hai = function()
// {
//     console.log("Hello broo!")
// } 
// hai()

// const gm = function(x)
// {
//     console.log("my branch is:",x)
// }
// gm("CSE")

// setTimeout(function () {
//   console.log("Hello after 1 second");
// }, 1000);

//Arrow functions....

// const gm = () =>
// {
//     console.log("hai")
// }
// gm()

// //arrow functions with parameters...
// const gm = (age) =>
// {
//     console.log("my age is :",age)
// }
// gm(20)


// callback function.....

// function boom(name,d)
// {
//     console.log("hai",name)
//     d()
// }
// function say()
// {
//     console.log("bye!")
// }
// boom("tanu",say)

// Higher-order Function...

// function operate(a, b, operation) {
//   return operation(a, b);
// }

// const add = (x, y) => x + y;
// console.log(operate(4, 5, add)); // 9


// const hai = (name , callback)=>{
//     console.log("hai")
//     callback()
// }

// hai("ram" , ()=>{
//     console.log("greeting done")
// })

// arr=[1,3,5,6,7,8]
// arr.forEach(function(item) {
//   console.log(item);
// });

// a=[1,2]
// p= a.includes(2);       // true
// a.indexOf(2);        // 1 return the position
// a.find(x => x > 1);  // 2
// a.filter(x => x > 1);// [2]
// console.log(p)

// arr=[1,4,5,7,8,,10]
// b=arr.filter((i) => i%2==0)
// {
//     console.log(b)
// }


// let arr = [1,2];
// let doubled = arr.map(x=> x*2);
// let sum = arr.reduce((acc,x) => acc +x, 0);

// let matrix = [[1, 2], [3, 4]];
// console.log(matrix[1][0]); // 3

// const [first, second] = [10, 20, 30];
// console.log(first); // 10

let car = {
  brand: "Toyota",
  model: "Innova",
  year: 2020
};
console.log(car.model);     // Dot notation use "." notation
console.log(car["brand"]); // Bracket notation use "[]" notations
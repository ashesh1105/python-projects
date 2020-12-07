var lbs = prompt("Enter number in pounds")
var kgs = lbs * 0.454
alert("The kgs equivalent is: " + kgs)
console.log("Conversion Completed!");

var temp = 50;
if (temp > 80) {
    console.log("Hot!");
} else if (temp < 80 && temp > 60) {
  console.log("Okay");
} else {
  console.log("Cold!");
}

var num = 10
while (num > 0) {
  console.log(num);
  num--
}

Will print 10 t0 4
var num = 10
while(true) {
  console.log(num);
  if (num < 5) {
    break
  }
  num--
}

for loop
word = "Hello"
for (i=0; i<word.length; i++) {
  console.log(word[i]);
}

Functons take keyword: function
var name = prompt("Enter your name")
// Define function
function hello(name) {
  console.log("Hello " + name + "!");
}
// Call the function
hello(name)

function addNums(num1, num2) {
  return num1 + num2
}
// Type conversion
let number1 = parseInt(prompt("Enter number 1"))
let number2 = parseInt(prompt("Enter number 2"))
console.log(addNums(number1, number2));

Arrays
let arr = []
// Can take mixed data types!
let arr1 = [2, "Ashesh", 34.5, true]
console.log("First array element:", arr1[0], "Last element:", arr1[3]);
// Doesn't give exceptions like ArrayIndexOutOfBounds exception like Java, just gives result as undefined
console.log(arr1[5]);
console.log(arr1.pop());
console.log("arr1 array now becomes:", arr1)

// Interesting for loop with Array
for (elem of arr1) {
  console.log(elem);
}

// Alerts users on browser with every element of array!
arr1.forEach(alert)

Maps
cars = {a: 'Honda', b: "Toyota", c: "BMW"}
console.log(cars);

for (k in cars) {
  console.log(k);
  console.log(cars[k])
}

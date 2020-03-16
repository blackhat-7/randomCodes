console.log("Hello World!");

let sum = function(x, y) {
    return x + y;
}

console.log(sum(5, 4));

let numbers = [1,2,3,4,5];

numbers.shift();
numbers.unshift('gay');
console.log(numbers);

const meals = ['breakfast', 'lunch', 'dinner' ];

meals.forEach(function(meal, i) {
    console.log("Meal number",i+1,':',meal);
} )
// constant variable type to store the days weather forecast in Kelvin unit. With a semicolon to close off the statement.
const kelvin = 293;

//Celcius is similar to Kelvin but 273 less than Kelvin. So by subtracting we'll have the correct Celcius number.
const celcius = kelvin - 273;
//let instead of const because of the next statement.
let fahrenheit = celcius * (9/5) + 32;

//The Math.floor() static method always rounds down and returns the largest integer less than or equal to a given number.
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`); 


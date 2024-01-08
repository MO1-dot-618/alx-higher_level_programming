#!/usr/bin/node
const args = process.argv.length - 2;
if (args < 2) {
  console.log('0');
}
else {
  const numbers = process.argv.slice(2).map(Number);
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}

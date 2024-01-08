#!/usr/bin/node
const n1 = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 1 || !n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(n1));

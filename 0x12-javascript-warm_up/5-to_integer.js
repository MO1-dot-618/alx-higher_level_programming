#!/usr/bin/node
const value = parseInt(process.argv[2]);
if (!isNaN(value)) {
  console.log(`My number: ${value}`);
} else {
  console.log('Not a number');
}

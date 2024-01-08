#!/usr/bin/node
const myVar = {
  c: 'C is fun',
  p: 'Python is cool',
  a: 'JavaScript is amazing'
};
for (const line in myVar) { 
console.log(myVar[line]);
}

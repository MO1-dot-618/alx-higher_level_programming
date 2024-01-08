#!/usr/bin/node
const myVar = {
  c: 'C is fun',
  p: 'Python is cool',
  a: 'Javascript is amazing'
};
for (const line in myVar) { 
console.log(myVar[line]);
}

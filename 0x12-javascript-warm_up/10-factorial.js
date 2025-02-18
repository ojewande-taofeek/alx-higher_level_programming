#!/usr/bin/node
const { argv } = require('node:process');

function factorial (a) {
  if (isNaN(a) || a === 0 || a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(argv[2]));

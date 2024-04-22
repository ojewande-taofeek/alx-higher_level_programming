#!/usr/bin/node
//  script that computes and prints a factorial
const { argv } = require('node:process');
function factorial (num) {
  if (Number(num)) {
    if (num === 0 || num === 1) {
      return (1);
    }
    return (num * factorial(num - 1));
  }
  return (1);
}
const fact = factorial(argv[2]);
console.log(fact);

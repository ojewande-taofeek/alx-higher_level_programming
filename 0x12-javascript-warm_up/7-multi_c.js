#!/usr/bin/node
// script that prints x times “C is fun”
const { argv } = require('node:process');
let first;
if (Number(argv[2])) {
  first = Number(argv[2]);
  while (first > 0) {
    console.log('C is fun');
    first--;
  }
} else {
  console.log('Missing number of occurrences');
}

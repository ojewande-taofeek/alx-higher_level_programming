#!/usr/bin/node
// script that prints a square
const { argv } = require('node:process');
let first, second;
if (Number(argv[2])) {
  first = Number(argv[2]);
  while (first > 0) {
    second = Number(argv[2]);
    console.log('X'.repeat(second));
    first--;
  }
} else {
  console.log('Missing size');
}

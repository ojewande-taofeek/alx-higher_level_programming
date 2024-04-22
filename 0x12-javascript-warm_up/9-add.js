#!/usr/bin/node
// script that prints the addition of 2 integers
const { argv } = require('node:process');
function add (a, b) {
  if (Number(argv[2])) {
    a = Number(argv[2]);
  }
  if (Number(argv[3])) {
    b = Number(argv[3]);
    console.log(a + b);
    return;
  }
  console.log(a + b);
}

add(argv[2], argv[3]);

#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log('0');
} else {
  const sortedArray = argv.slice(2).sort((a, b) => b - a);
  console.log(sortedArray[1]);
}

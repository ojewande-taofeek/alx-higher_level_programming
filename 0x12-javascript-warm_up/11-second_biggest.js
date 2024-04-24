#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const { argv } = require('node:process');
let argvLen = argv.length; // all cmd line input length
let count;
let argvCount = 2; // since args starts from index 2
let argvCpy;
const myList = [];
if (argvLen <= 3) {
  console.log(0);
} else {
  argvCpy = argv.slice(2); // copy of just the args
  argvLen = argvCpy.length; // just the args length
  for (count = 0; count < argvLen; count++, argvCount++) {
    if (Number(argv[argvCount])) { // check if it is a number
      myList[count] = argv[argvCount];
    }
  }
  myList.sort((a, b) => b - a); // to sort number in descending order
  console.log(myList[1]); // extract second largest
}

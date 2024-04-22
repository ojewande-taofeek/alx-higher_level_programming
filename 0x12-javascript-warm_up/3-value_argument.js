#!/usr/bin/node
/* script that prints the first argument passed to it */
const { argv } = require('node:process'); // same as let argv = process.argv
const argSlice = argv.slice(2); // make a cpy of argv from 2
if (argSlice[0] === undefined) {
  console.log('No argument');
} else {
  console.log(argSlice[0]);
}

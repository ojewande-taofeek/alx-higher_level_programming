#!/usr/bin/node
// Counting process.argv elements without length property
const { argv } = require('node:process');
if (argv.slice(2)[0] === undefined) {
  console.log('No arguments');
} else {
  console.log(argv[2]);
}

#!/usr/bin/node
//  script that prints two arguments passed to it, in the following format: ' is '
const { argv } = require('node:process');
if (argv.length === 2) {
  console.log('undefined is undefined');
} else if (argv.length === 3) {
  console.log(`${argv[2]} is undefined`);
} else {
  console.log(`${argv[2]} is ${argv[3]}`);
}

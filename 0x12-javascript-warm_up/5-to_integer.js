#!/usr/bin/node
/**
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(Number(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(argv[2])}`);
}

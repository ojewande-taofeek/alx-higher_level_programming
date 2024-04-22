#!/usr/bin/node
/*
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */
const { argv } = require('node:process');
if (Number(argv[2])) {
  console.log(argv[2]);
} else {
  console.log('Not a number');
}

#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < argv[2]; idx++) {
    console.log('C is fun');
  }
}

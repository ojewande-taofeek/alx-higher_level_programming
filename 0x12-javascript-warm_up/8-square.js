#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let row = 0; row < parseInt(argv[2]); row++) {
    console.log('X'.repeat(argv[2]));
  }
}

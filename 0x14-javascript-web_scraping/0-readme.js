#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs');
const process = require('node:process');
const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('Usage: ./0-readme.js <input_file>');
  process.exit(1);
}
const inputFile = argv[2];
fs.readFile(inputFile, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit(1);
  } else {
    console.log(data);
  }
});

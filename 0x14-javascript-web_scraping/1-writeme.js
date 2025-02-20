#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');
const { argv } = require('node:process');
const process = require('process');

if (argv.length < 4) {
  console.log('Usage: ./1-writeme.js <outputFile> <string_to_write>');
  process.exit(1);
}
const outputFile = argv[2];
const data = argv[3];
fs.writeFile(outputFile, data, (err) => {
  if (err) {
    console.log(err);
  }
});

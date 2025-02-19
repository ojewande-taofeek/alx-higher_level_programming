#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

if (argv.length < 5) {
  console.error('Usage: ./script.js <source_file1> <source_file2> ... <destination_file>');
  process.exit(1);
} else {
  const outputFile = argv[argv.length - 1];
  const allInputFiles = argv.slice(2, -1);
  allInputFiles.forEach((eachFile, index) => {
    fs.readFile(eachFile, 'utf-8', (err, data) => {
      if (err) {
        console.log(`Error reading ${eachFile}: ${err.message}`);
      } else {
        if (index === 0) {
          fs.writeFile(outputFile, data, (err) => {
            if (err) {
              console.log(`Error writing to ${outputFile}: ${err.message}`);
            }
          });
        } else {
          fs.appendFile(outputFile, data, (err) => {
            if (err) {
              console.log(`Error appending to ${outputFile}: ${err.message}`);
              process.exit(1);
            }
          });
        }
      }
    });
  });
}

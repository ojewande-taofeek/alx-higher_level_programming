#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const { argv } = require('node:process');
const fs = require('fs');
const process = require('process');

if (argv.length < 4) {
  console.log('Usage: ./5-request_store.js <url> <output_file>');
  process.exit(1);
} else {
  const url = argv[2];
  const outputFile = argv[3];

  request(url, (err, response) => {
    if (err) {
      console.log(err);
    } else {
      const responseObj = response.body;
      fs.writeFile(outputFile, responseObj, (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}

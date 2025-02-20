#!/usr/bin/node
// script that display the status code of a GET request.
const { argv } = require('node:process');
const request = require('request');
const process = require('process');

if (argv.length < 3) {
  console.log('Usage: ./2-statuscode.js <url>');
  process.exit(1);
} else {
  const url = argv[2];
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

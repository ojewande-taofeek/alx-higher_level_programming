#!/usr/bin/node
// reads and prints the content of a file.
const fs = require('fs');
const { argv } = require('node:process');
fs.readFile(argv[2], function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});

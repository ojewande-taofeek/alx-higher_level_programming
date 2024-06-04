#!/usr/bin/node
/*
 * writes a string to a file
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be written in utf-8
 * If an error occurred during while writing, print the error object
 */
const fs = require('fs');
const { argv } = require('node:process');
fs.writeFile(argv[2], argv[3], function (err) {
  if (err) {
    return console.log(err);
  }
});

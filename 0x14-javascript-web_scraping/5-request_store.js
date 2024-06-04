#!/usr/bin/node
//  gets the contents of a webpage and stores it in a file.
const request = require('request');
const { argv } = require('node:process');
const fs = require('fs');
request(argv[2]).pipe(fs.createWriteStream(argv[3]));

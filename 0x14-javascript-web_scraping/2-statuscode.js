#!/usr/bin/node
// display the status code of a GET request
const request = require('request');
const { argv } = require('node:process');
request(argv[2], function (error, response, body) {
  if (error || !error) { // error must be handeled, semistandard requirement
    console.log('code:', response.statusCode);
  }
});

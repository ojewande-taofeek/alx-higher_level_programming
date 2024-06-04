#!/usr/bin/node
// prints the title of a Star Wars movie where the
// episode number matches a given integer.
const request = require('request');
const { argv } = require('node:process');
let title;
let objJson;
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2] + '/';
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    objJson = JSON.parse(body);
    title = objJson.title;
    console.log(title);
  }
});

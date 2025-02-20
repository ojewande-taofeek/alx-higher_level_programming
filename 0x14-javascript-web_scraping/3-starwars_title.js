#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const process = require('process');
const { argv } = require('node:process');
const url = 'https://swapi-api.alx-tools.com/api/films/';

if (argv.length < 3) {
  console.log('Usage: ./3-starwars_title.js <id>');
  process.exit(1);
}
const id = argv[2];
const endpoint = `${url}${id}`;

request(endpoint, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const responseObj = JSON.parse(response.body); // convert the JSON from web to JS object
    console.log(responseObj.title);
  }
});

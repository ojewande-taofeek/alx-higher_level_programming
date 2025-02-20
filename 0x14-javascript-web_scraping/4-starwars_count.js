#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const { argv } = require('node:process');
const process = require('process');
const regex = /18\/$/;

if (argv.length < 3) {
  console.log('./4-starwars_count.js https://swapi-api.alx-tools.com/api/films');
  process.exit(1);
} else {
  const url = argv[2];
  request(url, (err, response) => {
    if (err) {
      console.log(err);
    } else {
      const responseObj = JSON.parse(response.body);
      const results = responseObj.results;
      let count = 0;
      results.forEach((element) => {
        const characters = element.characters;
        characters.forEach((peopleId) => {
          if (regex.test(peopleId)) {
            count++;
          }
        });
      });
      console.log(count);
    }
  });
}

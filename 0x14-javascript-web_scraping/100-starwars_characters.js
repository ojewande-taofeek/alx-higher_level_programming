#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const { argv } = require('node:process');
const request = require('request');
const process = require('process');

if (argv.length < 3) {
  console.log('Usage ./100-starwars_characters.js <movie_id>');
  process.exit(1);
} else {
  const movieId = argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  const endpoint = `${url}${movieId}`;
  request(endpoint, (err, response) => {
    if (err) {
      console.log(err);
    } else {
      const responseObj = JSON.parse(response.body);
      const characters = responseObj.characters;
      characters.forEach(characterURL => {
        request(characterURL, (err, characterResponse) => {
          if (err) {
            console.log(err);
          } else {
            const characterObj = JSON.parse(characterResponse.body);
            console.log(characterObj.name);
          }
        });
      });
    }
  });
}

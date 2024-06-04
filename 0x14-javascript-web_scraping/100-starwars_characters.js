#!/usr/bin/node
//  prints the number of movies where the
//  character “Wedge Antilles” is present
const request = require('request');
const { argv } = require('node:process');
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
let objJson;
let count = 0;
let character;
let characterLen;
let charResponse;
let charName;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    objJson = JSON.parse(body);
    character = objJson.characters;
    characterLen = character.length;
    for (; count < characterLen; count++) {
      request(character[count], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          charResponse = JSON.parse(body);
          charName = charResponse.name;
          console.log(charName);
        }
      });
    }
  }
});

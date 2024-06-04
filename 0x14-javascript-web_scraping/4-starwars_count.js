#!/usr/bin/node
//  prints the number of movies where the
//  character “Wedge Antilles” is present
const request = require('request');
const { argv } = require('node:process');
const url = argv[2];
const idUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let idCounter = 0;
let objJson;
let results;
let count;
let character;
let characterLen;
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    objJson = JSON.parse(body);
    results = objJson.results;
    count = results.length - 1;
    for (; count >= 0; count--) {
      character = results[count].characters;
      characterLen = character.length;
      for (; characterLen > 0; characterLen--) {
        if (character[characterLen] === idUrl) {
          idCounter++;
        }
      }
    }
    console.log(idCounter);
  }
});

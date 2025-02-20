#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const { argv } = require('node:process');
const request = require('request');
const process = require('process');
const { promisify } = require('util');

const requestPromise = promisify(request);
if (argv.length < 3) {
  console.log('Usage ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const endpoint = `${url}${movieId}`;

async function printCharacters () {
  try {
    const movieCharacters = await requestPromise(endpoint);
    const characters = JSON.parse(movieCharacters.body).characters;
    for (const characterURL of characters) {
      try {
        const characterResponse = await requestPromise(characterURL);
        const characterObj = JSON.parse(characterResponse.body);
        console.log(characterObj.name);
      } catch (err) {
        console.log(err);
      }
    }
  } catch (err) {
    console.log(err);
  }
}

printCharacters();

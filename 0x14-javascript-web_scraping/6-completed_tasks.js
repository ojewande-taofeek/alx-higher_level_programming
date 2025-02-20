#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
const { argv } = require('node:process');
const process = require('process');

if (argv.length < 3) {
  console.log('Usage ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos');
  process.exit(1);
} else {
  const url = argv[2];
  request(url, (err, response) => {
    if (err) {
      console.log(err);
    } else {
      const usersCompleted = {};
      const responseObj = JSON.parse(response.body);
      responseObj.forEach((element) => {
        if (element.completed) {
          const key = element.userId;
          if (key in usersCompleted) {
            usersCompleted[key] += 1;
          } else {
            usersCompleted[key] = 1;
          }
        }
      });
      console.log(usersCompleted);
    }
  });
}

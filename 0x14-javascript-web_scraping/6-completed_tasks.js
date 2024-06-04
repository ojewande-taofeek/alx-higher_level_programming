#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const { argv } = require('node:process');
let taskCompl;
const newDict = {};
let user = 1;
let todoResponse;
let todoLen;
request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  todoResponse = JSON.parse(body);
  for (; user <= 10; user++) {
    taskCompl = 0;
    todoLen = todoResponse.length - 1;
    for (; todoLen >= 0; todoLen--) {
      if (user === todoResponse[todoLen].userId) {
        if (todoResponse[todoLen].completed === true) {
          taskCompl++;
        }
      }
    }
    if (taskCompl !== 0) {
      newDict[String(user)] = taskCompl;
    }
  }
  console.log(newDict);
});

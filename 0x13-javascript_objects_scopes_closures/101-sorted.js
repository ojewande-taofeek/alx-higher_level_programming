#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  const value = dict[key];
  const keyList = [];
  if (value in newDict) {
    continue;
  } else {
    for (const eachKey in dict) {
      if (value === dict[eachKey]) {
        keyList.push(eachKey);
      }
    }
    newDict[value] = keyList;
  }
}
console.log(newDict);

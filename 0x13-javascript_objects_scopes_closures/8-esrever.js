#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  if (list.length > 0) {
    const newList = [];
    for (let idx = list.length - 1; idx >= 0; idx--) {
      newList.push(list[idx]);
    }
    return newList;
  }
};

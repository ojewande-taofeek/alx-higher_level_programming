#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  let listLen = (list.length) - 1;
  let update = 0;
  const newList = [];
  while (listLen >= 0) {
    newList[update] = list[listLen];
    update++;
    listLen--;
  }
  return (newList);
};

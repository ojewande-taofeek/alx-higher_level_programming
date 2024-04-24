#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let count;
  let num = 0;
  for (count = 0; count < len; count++) {
    if (searchElement === list[count]) {
      num++;
    }
  }
  return (num);
};

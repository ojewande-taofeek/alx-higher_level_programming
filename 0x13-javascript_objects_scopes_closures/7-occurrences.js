#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (Array(list).length > 0) {
    let occurences = 0;
    list.forEach(element => {
      if (element === searchElement) {
        occurences++;
      }
    });
    return occurences;
  }
};

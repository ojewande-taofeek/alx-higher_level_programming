#!/usr/bin/node
// function that converts a number from base 10 to another base passed as argument
// closure
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};

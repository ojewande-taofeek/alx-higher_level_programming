#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else if (c === 'C') {
      let count = 0;
      while (count < this.width) {
        console.log('C'.repeat(this.width));
        count++;
      }
    }
  }
};

#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let idx = 0; idx < this.height; idx++) {
        console.log(String(c).repeat(this.width));
      }
    }
  }
};

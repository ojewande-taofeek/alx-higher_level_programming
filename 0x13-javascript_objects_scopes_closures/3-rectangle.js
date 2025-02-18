#!/usr/bin/node
// class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      console.log('X'.repeat(this.width));
    }
  }
};

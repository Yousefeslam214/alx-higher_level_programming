#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;

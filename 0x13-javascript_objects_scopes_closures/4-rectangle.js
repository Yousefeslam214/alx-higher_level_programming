#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
  
  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.width *= 2
    this.height *= 2
  }
}

module.exports = Rectangle;

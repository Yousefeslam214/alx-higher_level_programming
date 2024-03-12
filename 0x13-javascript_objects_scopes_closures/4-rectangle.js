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
    let tamp = this.height
    this.height = this.width
    this.width = tamp
  }

  double () {
    this.width *= this.width
    this.height *= this.height
  }
}

module.exports = Rectangle;

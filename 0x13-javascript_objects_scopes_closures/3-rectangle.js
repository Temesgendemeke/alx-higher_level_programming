#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w * h) <= 0 || h === undefined || w === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
};

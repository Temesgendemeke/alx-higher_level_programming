#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w * h) <= 0 || h === undefined || w === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};

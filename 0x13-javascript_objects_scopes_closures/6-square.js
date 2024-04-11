#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let n = 0; n < this.width; n++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;

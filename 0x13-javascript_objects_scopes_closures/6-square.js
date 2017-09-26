#!/usr/bin/node

const pSquare = require('./5-square').Square;
exports.Square = Square;

function Square (size) {
  pSquare.call(this, size, size);
}

Square.prototype.charPrint = function (c = 'X') {
  let xStr = '';
  let i = 0;
  let j = 0;

  while (j < this.height) {
    xStr += c;
    j++;
  }
  while (i < this.height) {
    console.log(xStr);
    i++;
  }
};

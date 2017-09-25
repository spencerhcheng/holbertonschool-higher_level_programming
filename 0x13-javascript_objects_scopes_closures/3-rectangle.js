#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if ((w === 0 || w < 0 || w === undefined) || (h === 0 || h < 0 || h === undefined)) {
    return undefined;
  } else if ((w !== 0 || w > 0) && (w !== 0 || w > 0)) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    let xStr = '';
    let i = 0;
    let j = 0;

    while (j < this.width) {
      xStr += 'X';
      j++;
    }
    while (i < this.height) {
      console.log(xStr);
      i++;
    }
  };
};

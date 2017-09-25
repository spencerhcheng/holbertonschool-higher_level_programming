#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if ((w === 0 || w < 0 || w === undefined) || (h === 0 || h < 0 || h === undefined)) {
    return undefined;
  } else if ((w !== 0 || w > 0) && (w !== 0 || w > 0)) {
    this.width = w;
    this.height = h;
  }
};

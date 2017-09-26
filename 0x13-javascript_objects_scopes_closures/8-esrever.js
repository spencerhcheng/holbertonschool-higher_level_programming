#!/usr/bin/node

exports.esrever = function (list) {
  let newList = [];
  let i = list.length - 1;

  while (i >= 0) {
    newList.push(list[i]);
    i--;
  }
  return (newList);
};

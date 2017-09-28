#!/usr/bin/node

let list = require('./100-data.js')['list'];

console.log(list);

let newList = list.map(function (x, i) {
  return x * i;
});

console.log(newList);

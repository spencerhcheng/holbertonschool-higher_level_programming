#!/usr/bin/node

let myFile = process.argv[2];

const fs = require('fs');
fs.readFile(myFile, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});

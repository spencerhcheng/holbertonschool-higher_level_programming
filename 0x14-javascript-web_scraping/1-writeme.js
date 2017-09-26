#!/usr/bin/node

let myArgs = process.argv.slice(2);

const fs = require('fs');
fs.writeFile(myArgs[0], myArgs[1], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});

#!/usr/bin/node

let myFiles = process.argv.slice(2);

const fs = require('fs');

fs.readFile(myFiles[0], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  let aContent = data;
  fs.readFile(myFiles[1], 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
    let bContent = data;
    let cContent = aContent + bContent;
    fs.writeFile(myFiles[2], cContent, 'utf8', function (err) {
      if (err) {
        return console.log(err);
      }
    });
  });
});

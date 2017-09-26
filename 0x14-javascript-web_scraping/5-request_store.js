#!/usr/bin/node

let myUrl = process.argv[2];
let saveFile = process.argv[3];

const request = require('request');
request.get(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const fs = require('fs');
  fs.writeFile(saveFile, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});

#!/usr/bin/node

let myUrl = process.argv[2];
const request = require('request');

request.get(myUrl, function (err, res) {
  if (err) {
    console.log(err);
  }
  console.log('code: %s', res.statusCode);
});

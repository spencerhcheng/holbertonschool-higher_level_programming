#!/usr/bin/node

let myUrl = process.argv[2];
const request = require('request');

request.get(myUrl, function (res) {
  console.log('code: %s', res.statusCode);
});

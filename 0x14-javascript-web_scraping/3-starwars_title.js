#!/usr/bin/node

let epNumber = process.argv[2];
let myUrl = 'http://swapi.co/api/films/' + epNumber;
const request = require('request');

request.get(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let json = JSON.parse(body);
  console.log(json['title']);
});

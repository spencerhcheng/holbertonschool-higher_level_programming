#!/usr/bin/node

let epNumber = process.argv[2];
let myUrl = 'http://swapi.co/api/films/' + epNumber;
const request = require('request');

request.get(myUrl, function (error, response, url_body) {
  if (error) {
    console.log(error);
  }
  let json = JSON.parse(url_body);
  console.log(json['title']);
});

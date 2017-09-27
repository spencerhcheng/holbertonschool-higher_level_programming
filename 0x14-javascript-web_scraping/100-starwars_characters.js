#!/usr/bin/node

let myUrl = 'https://swapi.co/api/films/' + process.argv[2];
const request = require('request');
request.get(myUrl, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  let json = JSON.parse(body)['characters'];
  for (let i = 0; i < json.length; i++) {
    request.get(json[i], function (err, res, body) {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body)['name']);
    });
  }
});

#!/usr/bin/node

let myUrl = process.argv[2];
const request = require('request');
let count = 0;
request.get(myUrl, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  let json = JSON.parse(body);
  let filmsList = json['results'];
  for (let i = 0; i < filmsList.length; i++) {
    let charList = filmsList[i]['characters'];
    for (let j = 0; j < charList.length; j++) {
      if (charList[j] === 'https://swapi.co/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});

#!/usr/bin/node

let myUrl = 'https://swapi.co/api/films/' + process.argv[2];
const request = require('request');
const nameList = {};
let nameArray = [];

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
      let charNum = json[i].slice(-3).replace(/\//g, '');
      nameList[charNum] = JSON.parse(body)['name'];
      if (i === json.length - 1) {
        for (let key in nameList) {
          if (key.length === 1) {
            let singleDigKey = '0' + String(key);
            nameArray.push(singleDigKey + nameList[key]);
          } else {
            nameArray.push(key + nameList[key]);
          }
        }
        nameArray = nameArray.sort();
        for (let j = 0; j < nameArray.length; j++) {
          console.log(nameArray[j].slice(2));
        }
      }
    });
  }
});

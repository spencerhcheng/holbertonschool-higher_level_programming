#!/usr/bin/node

let myUrl = 'https://swapi.co/api/films/' + process.argv[2];
const request = require('request');
const nameList = {};
let nameArray = [];

request.get(myUrl, function (err, res, body) {
  if (err || res.statusCode !== 200) {
    return console.log(err);
  }
  let json = JSON.parse(body)['characters'];
  for (let i = 0; i < json.length; i++) {
    request.get(json[i], function (err, res, body) {
      if (err || res.statusCode !== 200) {
        return console.log(err);
      }
      let charNum = json[i].slice(-3).replace(/\//g, '');
      nameList[charNum] = JSON.parse(body)['name'];
      let size = Object.keys(nameList).length;
      if (size === json.length) {
        for (var key in nameList) {
          nameArray.push([parseInt(key), nameList[key]]);
        }
        printArr(nameArray);
      }
    });
  }
});

function printArr (list) {
  for (let i = 0; i < list.length; i++) {
    console.log(list[i][1]);
  }
}

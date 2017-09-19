#!/usr/bin/node

let myArgs = process.argv.slice(2);

function add (a, b) {
  console.log(a + b);
}

if (!myArgs[0] || !parseInt(myArgs[0]) || !parseInt(myArgs[1])) {
  console.log('NaN');
} else {
  add(parseInt(myArgs[0]), parseInt(myArgs[1]));
}

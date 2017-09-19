#!/usr/bin/node
let myNum = process.argv[2];

if (!isNaN(parseInt(myNum))) {
  console.log('My number: %d', (myNum));
} else {
  console.log('Not a number');
}

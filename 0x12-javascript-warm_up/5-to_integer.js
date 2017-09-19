#!/usr/bin/node
let myArgs = process.argv.slice(2);

if (!isNaN(parseInt(myArgs[0]))) {
  console.log('My number: %d', (myArgs[0] >> 0));
} else {
  console.log('Not a number');
}

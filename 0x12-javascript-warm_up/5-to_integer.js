#!/usr/bin/node
let myArgs = process.argv.slice(2);

if (!isNaN(Number(myArgs[0]))) {
  console.log((myArgs[0] >> 0));
} else {
  console.log('Not a number');
}

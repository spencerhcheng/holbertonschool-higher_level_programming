#!/usr/bin/node
let xTimes = process.argv[2];
let i = 0;
if (isNaN(parseInt(xTimes))) {
  console.log('Missing number of occurrences');
} else {
  while (i < xTimes) {
    console.log('C is fun');
    i++;
  }
}

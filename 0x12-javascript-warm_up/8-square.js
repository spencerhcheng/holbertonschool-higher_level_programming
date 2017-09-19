#!/usr/bin/node

let myNum = process.argv[2];

let i = 0;
let j = 0;
let xStr = '';

if (isNaN(parseInt(myNum))) {
  console.log('Missing size');
} else {
  while (i < myNum) {
    xStr += 'X';
    i++;
  }
  while (j < myNum) {
    console.log(xStr);
    j++;
  }
}

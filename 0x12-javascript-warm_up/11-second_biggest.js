#!/usr/bin/node

let myNums = process.argv.slice(2);

let i = 0;

while (i < myNums.length) {
  myNums[i] = parseInt(myNums[i]);
  i++;
}

function sortNumber (a, b) {
  return a - b;
}

myNums.sort(sortNumber);

if (!myNums[0] || myNums.length === 1) {
  console.log('0');
} else {
  console.log(myNums[myNums.length - 2]);
}

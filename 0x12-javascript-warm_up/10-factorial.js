#!/usr/bin/node

let myArgs = process.argv.slice(2);
let result = 0;

function printFact (num) {
  if (num === 1) {
    return 1;
  } else {
    return (printFact(num - 1) * num);
  }
}

if (!myArgs[0]) {
  result = 1;
} else {
  result = printFact(myArgs[0]);
}

console.log(result);

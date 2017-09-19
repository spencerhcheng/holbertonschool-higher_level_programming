#!/usr/bin/node
let myArgs = process.argv.slice(2);
if (!myArgs[0]) {
  console.log('No argument');
} else {
  console.log(myArgs[0]);
}

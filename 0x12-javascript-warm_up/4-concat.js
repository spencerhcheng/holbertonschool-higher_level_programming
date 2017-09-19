#!/usr/bin/node
let myArgs = process.argv.slice(2);
let concatStr = myArgs[0] + ' is ' + myArgs[1];
console.log(concatStr);

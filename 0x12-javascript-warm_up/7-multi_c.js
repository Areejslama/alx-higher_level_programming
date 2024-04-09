#!/usr/bin/node

let num = 0;
const n = ['C is fun'];
const argv = process.argv;
const x = argv[2];
const str = parseInt(x);

if (isNaN(str)) {
  console.log('Missing number of occurrences');
} else {
  while (num < str) {
    console.log(n[0]);
    num++;
  }
}

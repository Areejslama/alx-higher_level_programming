#!/usr/bin/node

const argv = process.argv;
const num = argv[2];
const str = parseInt(num);

if (isNaN(str)) {
  console.log('Not a number');
} else {
  console.log('My number:', str);
}

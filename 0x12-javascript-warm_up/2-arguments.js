#!/usr/bin/node

const argv = process.argv;
const num = argv.length - 2;

if (num === 0) {
  console.log('No argument');
} else if (num === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

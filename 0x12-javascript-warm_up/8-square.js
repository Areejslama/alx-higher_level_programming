#!/usr/bin/node

const x = Number(process.argv[2]);

if (process.argv[2] === undefined || isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < str; i++) {
    console.log('x'.repeat(x));
  }
}

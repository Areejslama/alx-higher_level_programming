#!/usr/bin/node

const str = Number(process.argv[2]);

if (process.argv[2] === undefined || isNaN(str)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < str; i++) {
    console.log('x'.repeat(str));
  }
}

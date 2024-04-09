#!/usr/bin/node

const str = parseInt(process.argv[2]);

if (isNaN(str)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < str; i++) {
    console.log('x'.repeat(str));
  }
}

#!/usr/bin/node

const args = parseInt(process.argv[2]);

if (isNaN(args)) {
  console.log(0);
} else if (args === 0) {
  console.log(0);
} else if (args === 1) {
  console.log(1);
} else {
  console.log(args);
}

#!/usr/bin/node

const argv = process.argv;
const size = argv[2];
const str = parseInt(size);

if (isNaN(str)) {
    console.log('Missing size');
} else {
    for (let num = 0; num < str; num++) {
        let row = '';
        for (let i = 0; i < str; i++) {
            row += 'x';
        }
        console.log(row);
    }
}

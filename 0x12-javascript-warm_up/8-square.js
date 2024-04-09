#!/usr/bin/node

const str = parseInt(process.argv[2]);

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

#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }
print() {
        for (let n = 0; n < this.width; n++) {
		let row = '';
		for (let i = 0; i < this.height; i++) {
			row += 'x'
	}
		console.log(row);
    }
}
}
module.exports = Rectangle;

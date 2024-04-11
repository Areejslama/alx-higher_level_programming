#!/usr/bin/node

function nbOccurencess (list, searchElement) {
  let num = 0;
  for (let n = 0; n < list.length; n++) {
    if (list[n] === searchElement) {
      num++;
    }
  }
  return num;
}
exports.nbOccurences = nbOccurencess;

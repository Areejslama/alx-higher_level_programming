#!/usr/bin/node

function esrever (list) {
  const i = [];
  for (let n = list.length - 1; n >= 0; n--) {
    i.push(list[n]);
  }
  return i;
}
exports.esrever = esrever;

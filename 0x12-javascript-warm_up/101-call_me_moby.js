#!/usr/bin/node

exports.callMeMoby = function (x, thefunction) {
  for (let i = 0; i < x; i++) { thefunction(); }
};

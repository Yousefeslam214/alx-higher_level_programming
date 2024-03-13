#!/usr/bin/node
let globalVar = 0;
exports.logMe = function (item) {
  console.log(globalVar + ': ' + item);
  globalVar++;
};

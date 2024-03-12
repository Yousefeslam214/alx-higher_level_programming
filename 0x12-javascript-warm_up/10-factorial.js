#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log(1);
} else {
  console.log(secondBiggestNum(args[0]));
}

function secondBiggestNum (factorialNumber) {
  if (factorialNumber === 1) {
    return 1;
  }
  return secondBiggestNum(factorialNumber - 1) * factorialNumber;
}

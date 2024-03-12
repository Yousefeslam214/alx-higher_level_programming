#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log(1);
} else {
  console.log(factorial(args[0]));
}

function factorial (factorialNumber) {
  if (factorialNumber === 1) {
    return 1;
  }
  return factorial(factorialNumber - 1) * factorialNumber;
}

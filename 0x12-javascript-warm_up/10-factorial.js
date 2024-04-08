#!/usr/bin/node

const fact = parseInt(process.argv[2]);

if (isNaN(fact)) {
  console.log(1);
} else {
  console.log(factorial(fact));
}
function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return (num * factorial(num - 1));
}

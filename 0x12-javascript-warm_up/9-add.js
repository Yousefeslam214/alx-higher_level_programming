#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || !args[1]) {
  console.log('NaN');
} else if (!isNaN(args[1])) {
  console.log(parseInt(args[0]) + parseInt(args[1]));
}

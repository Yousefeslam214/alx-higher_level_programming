#!/usr/bin/node
const args = process.argv.slice(2);
const argsAranged = args.sort((a, b) => a - b);
if (isNaN(args[0]) || !args[1]) {
  console.log(0);
} else {
  console.log(argsAranged[argsAranged.length - 2]);
}

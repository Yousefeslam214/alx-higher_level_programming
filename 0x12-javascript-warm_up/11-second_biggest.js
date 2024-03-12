#!/usr/bin/node
const args = (process.argv.slice(2)).sort();
if (isNaN(args[0]) || !args[1]) {
  console.log(0);
} else {
  console.log(args[args.length - 2]);
}

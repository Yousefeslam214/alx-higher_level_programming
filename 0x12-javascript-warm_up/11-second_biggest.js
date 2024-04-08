#!/usr/bin/node

if (!(process.argv[3])) {
  console.log('0');
} else {
  let i = 2;
  let j = 0;
  let arr = [];
  while (process.argv[i]) {
    arr[j] = parseInt(process.argv[i]);
    j++;
    i++;
  }
  arr = arr.sort((a, b) => b - a);
  console.log(arr[1]);
}

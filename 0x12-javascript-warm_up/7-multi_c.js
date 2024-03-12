#!/usr/bin/node
const args = process.argv.slice(2);
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
while (i < 3) {
  console.log(arr[i]);
  i++;
}

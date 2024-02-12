#!/usr/bin/node
const arr = process.argv;
let first = arr[2];
let second = first;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < arr.length; i++) {
    for (let j = 2; j < arr.length; j++) {
      if (first < arr[i + 1]) {
        second = first;
        first = arr[i + 1];
      }
    }
  }
  console.log(second);
}

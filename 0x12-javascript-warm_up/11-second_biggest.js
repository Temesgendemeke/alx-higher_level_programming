#!/usr/bin/node
const arr = process.argv;
let temp = arr[2];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < arr.length; i++) {
    for (let j = 2; j < arr.length; j++) {
      if (temp < arr[i + 1]) {
        temp = arr[i + 1];
      }
    }
  }
  console.log(temp);
}

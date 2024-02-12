#!/usr/bin/node
const arr = process.argv;

if (arr.length <= 3) console.log(0);
else {
  const list = arr.sort();
  console.log(list.reverse()[1]);
}

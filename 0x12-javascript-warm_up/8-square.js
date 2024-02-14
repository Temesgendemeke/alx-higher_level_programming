#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) console.log('Missing size');
else if (size > 0) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
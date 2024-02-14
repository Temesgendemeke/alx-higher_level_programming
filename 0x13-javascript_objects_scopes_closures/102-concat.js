#!/usr/bin/node
const files = process.argv;

file1 = require('./' + files[2]);
file2 = require('./' + files[3]);
file3 = require('./' + files[4]);

file3.writeFile(files3, file1.readFile(file1));

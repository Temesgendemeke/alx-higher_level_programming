#!/usr/bin/node
const fs = require('node:fs');

const content = fs.readFileSync(process.argv[2], 'utf-8');
console.log(content);

#!/usr/bin/node
const dict = require('./101-data').dict;
const dict2 = {};

for (const [key, value] of Object.entries(dict)) {
  const Ky = key;
  for (const [key, value] of Object.entries(dict)) {
    if (dict[Ky] === dict[key]) {
      dict2[value] = Array.prototype.map.call(dict, (key) => key / 2);
    }
  }
}

console.log(dict2);

#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  let count = 0;
  const obj = JSON.parse(body);
  for (const key in obj.results) {
    for (const i in (obj.results[key].characters)) {
      if (obj.results[key].characters[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});

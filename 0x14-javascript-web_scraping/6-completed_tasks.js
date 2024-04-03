#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    const dumpObj = {};

    for (const i in obj) {
      let count = 0;
      const id = obj[i].userId;

      for (const j in obj) {
        if (obj[j].completed && obj[j].userId === id) {
          count++;
        }
      }
      dumpObj[id] = count;
    }
    console.log(dumpObj);
  }
});

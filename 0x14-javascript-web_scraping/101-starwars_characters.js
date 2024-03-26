#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const obj = JSON.parse(body);
  const charObj = obj.characters;
  print(charObj, 0);
});

function print (charObj, i) {
  request(charObj[i], (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const name = JSON.parse(body).name;
    console.log(name);
    if (i + 1 < charObj.length) {
      print(charObj, i + 1);
    }
  });
}

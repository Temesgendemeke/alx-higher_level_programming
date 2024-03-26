#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const obj = JSON.parse(body);
  for (const people in obj.characters) {
    const peopleUrl = obj.characters[people];
    request(peopleUrl, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const parseObj = JSON.parse(body);
      console.log(parseObj.name);
    });
  }
});

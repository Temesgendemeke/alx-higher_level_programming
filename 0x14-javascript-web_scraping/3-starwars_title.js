#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, reponse, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});

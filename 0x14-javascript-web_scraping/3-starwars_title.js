#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, resource, body) => {
  if (error) {
    console.log(`code: ${resource.statusCode}`);
    return;
  } else {
    console.log((JSON.parse(body)).title);
  }
});

#!/usr/bin/node

const request = require('request');
// const request = require("request");
const url = process.argv[2];

request.get(url, (error, resource, body) => {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    const films = body.results;
    console.log(countMoviesWithId(18, films));
  }
});

function countMoviesWithId (id, films) {
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes(id)) {
        count++;
      }
    }
  }
  return count;
}

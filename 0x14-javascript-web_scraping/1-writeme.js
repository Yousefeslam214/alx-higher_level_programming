#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[3], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});

#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, resource, body) => {
  if (error) {
    console.error(error);
  }

  const todoUser = JSON.parse(body);
  const completedTasks = {};
  for (const todo of todoUser) {
    if (todo.completed) {
      const userId = todo.userId;
      console.log(completedTasks[userId])
      if (completedTasks[userId]) {
        completedTasks[userId] += 1
      } else {
        completedTasks[userId] = 1
      }
    }
  }
  console.log(completedTasks)
});

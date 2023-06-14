#!/usr/bin/node

const array = require('./100-data').list;

console.log(array);

const newArray = array.map(x => x * 2);
console.log(newArray);

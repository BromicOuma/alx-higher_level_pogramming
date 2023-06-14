#!/usr/bin/node

const array = require('./100-data').list;

console.log(array);

const newArray = array.map((x, idx) => x * idx);
console.log(newArray);

#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (!x || (process.argv.length < 3)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}

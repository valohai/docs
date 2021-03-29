const sass = require('node-sass');
const cssnano = require('cssnano');
const fs = require('fs');

const renderSass = (options) => (
  new Promise((resolve, reject) =>
    sass.render(options, (err, result) => {
      if (err) return reject(err);
      resolve(result);
    })
  )
);


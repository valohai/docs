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

renderSass({
  file: 'source/_themes/valodoc/static_src/valodoc.scss',
  includePaths: ['source/_themes/valodoc/static_src'],
})
  .then((result) => result.css.toString())
  .then((css) => cssnano.process(css, {mergeRules: false}))
  .then((result) => result.css.replace(/\}/g, '}\n'))
  .then((css) => {
    fs.writeFileSync('source/_themes/valodoc/static/valodoc.css', css, 'UTF-8');
    console.log(`OK, ${css.length} bytes`);
  })
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });

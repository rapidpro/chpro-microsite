/**
* Compare a variable against a string
 *
 * @param {object} handlebars The global Handlebars object used by kss-node's kssHandlebarsGenerator.
 */

module.exports = function(handlebars) {
  handlebars.registerHelper('if_equal', function(base, string, opts) {
    if (base == string) {
      return opts.fn(this)
    } else {
      return opts.inverse(this)
    }
  });
};

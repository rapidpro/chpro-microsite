RapidPro Health Style Guide
===============

You can use this guide to develop new content for the website, rapidpro.com. This guide is by no means exhaustive but should cover the essentials for creating excellent looking content.

As of March 2018, this guide is a work in progress.

##### Browser Support

Vendor prefixes happen with autoprefixer and Parcel. To see a list of browsers the project is supporting, run `yarn check_browserlist`. Update this list in the file `/rh/client/.browserlistrc`.

##### Working with Scss

See the [Compiling](https://github.com/rapidpro/chpro-microsite/blob/master/docs/local_install.md#compiling) section of this [project's README](https://github.com/rapidpro/chpro-microsite/blob/master/docs/local_install.md) file to get instructions on how to compile front-end assets.

We use Foundation as our base framework. By default, we [do not include](https://foundation.zurb.com/sites/docs/sass.html#adjusting-css-output) all Foundation styles for performance reasons. Please refer the application's [Foundation manifest](https://github.com/rapidpro/chpro-microsite/blob/master/rh/client/scss/_foundation.scss) to see which files are currently included, and if you wish, uncomment to include any other files.

##### External Documentation

* [kss-node](https://github.com/kss-node/kss-node) - The generator for this style guide
* [KSS](http://warpspire.com/kss/) - The specification for comments
* [Markdown Syntax](https://daringfireball.net/projects/markdown/syntax) - Usable in comments
* [Browserlist documentation](https://www.npmjs.com/package/browserslist) - Autoprefixer queries


## This Styleguide

##### Contributing

This styleguide is built using [kss-node](https://github.com/kss-node/kss-node) which is a npm implementation of [KSS](http://warpspire.com/kss/). KSS parses comments in SCSS code and generates this documentation. Typical KSS comments look like this:

<div class="kss-markup kss-style"><pre class="prettyprint linenums lang-css"><code data-language="css">// Name of Section
//
// Some Markdown text describing what's going on. Try to leave good comments!
//
// Markup: file_name.hbs
//
// Weight: [number]
//
// Style guide: section.subsection
</code></pre></div>

##### Making Theme Changes

The theme used by kss-node can be found `docs/_templates/styleguide-template`.

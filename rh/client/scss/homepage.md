RapidPro Health Style Guide
===============

You can use this guide to develop new content for the website, rapidpro.com. This guide is by no means exhaustive but should cover the essentials for creating excellent looking content.

As of March 2018, this guide is a work in progress.



#### External Documentation

* [kss-node](https://github.com/kss-node/kss-node) - The generator for this style guide
* [KSS](http://warpspire.com/kss/) - The specification for comments
* [Markdown Syntax](https://daringfireball.net/projects/markdown/syntax) - Usable in comments



## Contributing

This styleguide is built using [kss-node](https://github.com/kss-node/kss-node) which is a npm implementation of [KSS](http://warpspire.com/kss/). KSS parses comments in SCSS code and generates this documentation. Typical KSS comments look like this:

<div class="kss-markup kss-style"><pre class="prettyprint linenums lang-css"><code data-language="css">// Name of Section
//
// Some Markdown text describing what's going on. Try to leave good comments!
//
// Markup: ../../../../docs/styleguide/file_name.html
//
// Weight: [number]
//
// Style guide: section.subsection
</code></pre></div>

### Making Theme Changes

The theme used by kss-node can be found `docs/_templates/styleguide-template`.

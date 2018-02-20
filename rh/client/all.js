import './scss/core.scss';

import jQuery from "jquery";
window.$ = window.jQuery = jQuery;

import * as Foundation from 'foundation-sites';

// initialize standalone plugins/widgets
$(document).foundation();

import './js/app';

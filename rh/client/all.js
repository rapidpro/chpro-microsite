import './scss/core.scss';

import jQuery from "jquery";
window.$ = window.jQuery = jQuery;

import * as Foundation from 'foundation-sites';
import './js/app';

// initialize standalone plugins/widgets
$(document).foundation();

// initialize standalone plugins/widgets
import $ from  './import-jquery';

import 'foundation-sites';

$(document).ready(() => {
  $(document).foundation();

  if ($('.case-study-search-filters').length > 0){
    if (Foundation.MediaQuery.atLeast('medium')) {
      $('.case-study-search-filters').foundation('down', $('.case-study-search-list'), false);
    }

    $(window).on('changed.zf.mediaquery', function(event, newSize, oldSize) {
      if (newSize !== oldSize) {
        $('.case-study-search-filters').foundation('down', $('.case-study-search-list'), true);
      }
    });
  }

  //$('.featured-accordion').foundation('selectTab', 'card');
  $('.featured-accordion').on('change.zf.tabs', function() {
     if ($('#card1:visible').length) {
         console.log('Tab 1 panel shown.');
     }
     if ($('#card2:visible').length) {
         console.log('Tab 2 panel shown.');
     }
  });
});

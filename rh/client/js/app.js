// initialize standalone plugins/widgets
import $ from  './import-jquery';

import 'foundation-sites';

$(document).ready(() => {
  $(document).foundation();

  if ($(".case-study-search-filters").length ){
    if (Foundation.MediaQuery.atLeast('medium')) {
      $('.case-study-search-filters').foundation('down', $('.case-study-search-list'), false);
    }

    $(window).on('changed.zf.mediaquery', function(event, newSize, oldSize) {
      if (newSize !== oldSize) {
        $('.case-study-search-filters').foundation('down', $('.case-study-search-list'), true);
      }
    });
  }
});

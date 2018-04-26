// initialize standalone plugins/widgets
import $ from  './import-jquery';

import 'foundation-sites';

$(document).ready(() => {
  $(document).foundation();

  // Case study filters
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

  // Featured accordion
  if ($('.featured-accordion').length > 0){
    $('.featured-accordion-cards .card').click(function(event) {
      event.preventDefault();
    });

    $('.featured-accordion .card-actions a').click(function(event) {
      window.location.href = $(this).attr('href');
    });
  }
});

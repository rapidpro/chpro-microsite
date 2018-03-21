/**
 * Icon & Color select2 and WYSIWYG
 */
(function($) {
// Apply Icon Chooser to existing elements
// TODO: The code below should only run if necessary
  applyIconSelector();

  // Apply fixes and editor setup whenever a new inline appears
  $(document).on('formset:added', function(event, $row) {
    // TODO: Icon, color, WYSIWG should only run if necessary
    applyIconSelector($row);              // SVG Icon dropdown
  });

})(window.django.jQuery);


/**
 * Icon select2 and WYSIWYG
 */
(function($) {
// Apply Icon Chooser to existing elements
// TODO: The code below should only run if necessary
  if (!$){
    return;
  }

  applyIconSelector();

  // Apply fixes and editor setup whenever a new inline appears
  $(document).on('formset:added', function(event, $row) {
    // TODO: Icon, color, WYSIWG should only run if necessary
    applyIconSelector($row); // SVG Icon dropdown
  });

  if(typeof(CKEDITOR) !== 'undefined') {
    CKEDITOR.editorConfig = function(config) {
      config.skin = 'icy_orange';
      config.contentsCss = [
        '/static/css/styles.css'  // Is there a way to not hardcode this?
      ];

      config.stylesSet.add('default', [
        {
          name: 'Lead Paragraph',
          element: 'p',
          attributes: { 'class': 'lead' }
        },
        {
          name: 'Stat',
          element: 'span',
          attributes: { 'class': 'stat' }
        }
      ]);
    }
  }
})(window.django && window.django.jQuery || window.jQuery);

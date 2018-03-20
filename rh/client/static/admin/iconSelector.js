// Icon selector
function applyIconSelector($elem){
  let selector = '.icon-selector';
  if ($elem && $elem.length > 0){

    // reset select2 classes applied to previous row
    $elem.find('.select2').remove();
    selector = $elem.find(selector).removeClass('select2-hidden-accessible');
  }

  $(selector).select2({
    templateResult: function(state) {
      if (!state.id) { return state.text; }
      let $state;
      let icon;
      const baseName = state.element.value.toLowerCase();

      if (baseName.search('uploaded-svg-file') !== -1){
        icon = '<img class="icon icon-medium" src="'+window.rh.uploadedSvgIcons[baseName]+'"/>';
      } else {
        icon = '<svg class="icon icon-medium"><use xlink:href="/static/icons/sprite.svg#'+baseName+'"></use></svg>';
      }

      $state = $(
        '<span class="select2-svg-result">'
          + icon +
        ' <strong class="select2-svg-result-name">'
          + state.text +
        '</strong></span>'
      );
      return $state;
    }
  });
}

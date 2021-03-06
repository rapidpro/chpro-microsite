// Icon selector
function applyIconSelector($elem){
  let selector = '.icon-selector';
  if ($elem && $elem.length > 0){

    // reset select2 classes applied to previous row
    $elem.find('.select2').remove();
    selector = $elem.find(selector).removeClass('select2-hidden-accessible');
  }

  $(selector).select2({
    allowClear: true,
    placeholder: "Search for an icon",
    templateResult: function(state) {
      if (!state.id) { return state.text; }
      var $state;
      var icon;
      var baseName = state.element.value.toLowerCase();

      if (baseName.search('uploaded-svg-file') !== -1){
        icon = '<img class="icon" src="'+window.rh.uploadedSvgIcons[baseName]+'"/>';
      } else {
        icon = '<svg class="icon"><use xlink:href="/static/img/sprite.svg#'+baseName+'"></use></svg>';
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

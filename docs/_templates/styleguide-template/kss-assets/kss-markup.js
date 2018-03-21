(function (window, document) {
  'use strict';

  var KssMarkup = function (config) {
    this.bodyClass = config.bodyClass || 'kss-markup-mode';
    this.detailsClass = config.detailsClass || 'kss-markup';

    this.init();
  };

  KssMarkup.prototype.init = function () {
    var self = this;
    // Initialize all markup toggle buttons.
    document.querySelectorAll('a[data-kss-markup]').forEach(function (el) {
      el.onclick = self.showGuides.bind(self);
    });
  };

  // Export to DOM global space.
  window.KssMarkup = KssMarkup;

})(window, document);

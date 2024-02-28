$(document).ready(function() {
  $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      method: 'GET',
      dataType: 'json',
      success: function(data) {
        $('DIV#hello').text(data.hello);
      }
  });
});

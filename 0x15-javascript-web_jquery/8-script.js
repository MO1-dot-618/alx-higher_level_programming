$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      // Assuming data is an array of films
      $.each(data.results, function(index, film) {
        $('ul#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});

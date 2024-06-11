/*
Fetches and lists the title for all movies by using
this URL: https://swapi-api.alx-tools.com/api/films/?format=json
*/
$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    const films = data.results;
    const filmsLen = films.length;
    for (let count = 0; count < filmsLen; count++) {
      $('UL#list_movies').append('<li>' + films[count].title + '</li>');
    }
  });

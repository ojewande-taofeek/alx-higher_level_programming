const url = "https://swapi-api.alx-tools.com/api/films/?format=json";

$.get(url, ((data) => {
  const allMovies = data.results;
  for (const eachMovie of allMovies) {
    $('ol#list_movies').append(`<li>${eachMovie.title}</li>`);
  }
}))
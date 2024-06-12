$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (movies, textStatus) {
    $.each(movies.results, function (index, movie) {
        $("#list_movies").append(`<li>${movie.title}</li>`);
    });
});
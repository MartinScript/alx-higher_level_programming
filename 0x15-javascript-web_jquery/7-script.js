#!/usr/bin/node
$.get("https://swapi-api.alx-tools.com/api/people/5/?", function (data, textStatus) {
    $("#character").text(data.name);
});
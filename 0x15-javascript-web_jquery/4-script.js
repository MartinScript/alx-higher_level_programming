#!/usr/bin/node
$(function () {
    $("#toggle_header").on("click", function () {
        if ($("header").hasClass("red"))
            $("header").toggleClass("green");
        else if ($("header").hasClass("green")) {
            $("header").toggleClass("red");
        };
    });
});
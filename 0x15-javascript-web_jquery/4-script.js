$(document).ready(function() {
    $("DIV#toggle_header").click(function() {
         let header = $("header");
         let currentClass = header.attr("class");
         let newClass = currentClass === "red" ? "green" : "red";
         header.removeClass(currentClass); // Remove the current class
         header.addClass(newClass);     // Add the new class
    });
});
$(document).ready(function () {
    $("ul.projects_list li:even").addClass("alt");
    
    //User dropdown
    $('div.user').click(function () {
        $('ul.user').slideToggle('fast');
    });
    
    //Type dropdown
    $('div.type').click(function () {
        $('ul.type').slideToggle('fast');
    });
    
    //Syntax list
    $('a.syntax_guide_link').click(function () {
       $('div.syntax_guide').slideToggle('fast');
    });
    
});
$(document).ready(function () {
    
    $('.inplace input').mouseout(function () {
        $(this).css({ 'border' : '1px solid #d2d2d2', 'background-color' : '#ffffff' });
    });

    $('.inplace input').mouseover(function () {
        $(this).css({ 'border' : '1px solid transparent', 'background-color' : 'transparent' });
    });
    
    $('.inplace textarea').mouseout(function () {
        $(this).css({ 'border' : '1px solid #d2d2d2', 'background-color' : '#ffffff' });
    });

    $('.inplace textarea').mouseover(function () {
        $(this).css({ 'border' : '1px solid transparent', 'background-color' : 'transparent' });
    });
    
});
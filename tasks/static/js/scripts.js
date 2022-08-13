$( document ).ready(function() {

    var deleteBnt = $('delete-btn');

    $(deleteBtn).on('click', function(e) {
        
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if(refult) {
            window.location.href = delLink;
        }
    });

});
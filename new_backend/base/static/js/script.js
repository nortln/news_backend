$(window).scroll(function() {
    if ($(window).scrollTop() + $(window).height() >= $(document).height() - 100) {
        loadMoreNews();
    }
});

function loadMoreNews() {
    let nextPage = $('.news-container').data('next-page');
    if (nextPage) {
        $.ajax({
            url: window.location.href,
            data: { page: nextPage },
            headers: { 'X-Requested-With': 'XMLHttpRequest' },
            success: function(response) {
                // Append new news items
                $('.news-container').data('next-page', response.has_next ? nextPage + 1 : null);
            }
        });
    }
}

$('.like-btn').click(function() {
    const newsId = $(this).data('news-id');
    $.post(`/news/${newsId}/like/`, function(response) {
        // Update like count
    });
});

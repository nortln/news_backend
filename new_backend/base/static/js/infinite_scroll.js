$(document).ready(function() {
    let loading = false;
    
    $(window).scroll(function() {
        if ($(window).scrollTop() + $(window).height() >= $(document).height() - 100 && !loading) {
            loadMoreNews();
        }
    });

    function loadMoreNews() {
        loading = true;
        $('#loading').show();
        
        let nextPage = $('.news-container').data('next-page');
        if (nextPage) {
            $.ajax({
                url: window.location.href,
                data: { page: nextPage },
                headers: { 'X-Requested-With': 'XMLHttpRequest' },
                success: function(response) {
                    if (response.news.length > 0) {
                        response.news.forEach(function(news) {
                            let imageHtml = news.image ? 
                                `<div class="image-container">
                                    <img src="${news.image}" alt="${news.title}" class="news-image">
                                </div>` : 
                                '';
                            let newsItem = `
                                <div class="news-item mb-4">
                                    <h2><a href="${news.url}">${news.title}</a></h2>
                                    ${imageHtml}
                                    <p>${news.content}</p>
                                    <div class="news-meta">
                                        <span class="badge bg-secondary">Views: ${news.views}</span>
                                        <span class="badge bg-success">Likes: ${news.likes}</span>
                                        <span class="badge bg-info">Published: ${news.created_at}</span>
                                    </div>
                                </div>`;
                            $('.news-container').append(newsItem);
                        });
                        $('.news-container').data('next-page', response.has_next ? nextPage + 1 : null);
                    }
                },
                complete: function() {
                    loading = false;
                    $('#loading').hide();
                }
            });
        }
    }
});
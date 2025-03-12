from django.contrib import admin
from .models import News, Tag, NewsLike

class NewsLikeInline(admin.TabularInline):
    model = NewsLike
    extra = 0

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'created_at')
    list_filter = ('tags', 'created_at')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)
    inlines = [NewsLikeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'news_count')
    
    def news_count(self, obj):
        return obj.news.count()
    news_count.short_description = 'Number of News'

@admin.register(NewsLike)
class NewsLikeAdmin(admin.ModelAdmin):
    list_display = ('news', 'ip_address', 'created_at')
    list_filter = ('created_at', 'news')
    search_fields = ('ip_address', 'news__title')

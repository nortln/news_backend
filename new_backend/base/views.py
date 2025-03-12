from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import News, Tag, NewsLike
from django.db import models

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        news_data = [{
            'title': item.title,
            'content': item.content[:200],
            'image': item.image.url if item.image else None,
            'url': item.get_absolute_url(),
            'views': item.views,
            'likes': item.likes.count(),
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M'),
        } for item in page_obj.object_list]
        return JsonResponse({'news': news_data, 'has_next': page_obj.has_next()})
    
    return render(request, 'list.html', {'page_obj': page_obj})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.views += 1
    news.save()
    return render(request, 'detail.html', {
        'news': news,
        'likes_count': news.likes.count()
    })

def news_by_tag(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    news = tag.news.all().order_by('-created_at')
    return render(request, 'by_tag.html', {'news': news, 'tag': tag})

def news_statistics(request):
    most_viewed = News.objects.order_by('-views')[:10]
    most_liked = News.objects.annotate(likes_count=models.Count('likes')).order_by('-likes_count')[:10]
    return render(request, 'statistics.html', {
        'most_viewed': most_viewed,
        'most_liked': most_liked
    })

def like_news(request, pk):
    if request.method == 'POST':
        news = get_object_or_404(News, pk=pk)
        ip = request.META.get('REMOTE_ADDR')
        
        if not NewsLike.objects.filter(news=news, ip_address=ip).exists():
            NewsLike.objects.create(news=news, ip_address=ip)
        
        return JsonResponse({
            'success': True,
            'likes_count': news.likes.count()
        })
    return JsonResponse({'success': False}, status=400)

from django.contrib import admin
from .models import News, News_Category, Gallery_Category, Gallery
from django_summernote.admin import SummernoteModelAdmin

class NewsAdmin(SummernoteModelAdmin):    
    list_display = ('id', 'title', 'status', 'created_on')
    list_display_links = ('id', 'title')
    list_filter = ('status',)
    lists_per_page = 25
    search_fields = ['title']
    summernote_fields = ('content', )

admin.site.register(News, NewsAdmin)
admin.site.register((News_Category, Gallery_Category, Gallery))


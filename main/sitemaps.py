from django.contrib.sitemaps import Sitemap
from main.models import News

class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def items(self):
        return News.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.created_on
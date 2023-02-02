from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from taggit.managers import TaggableManager 


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BaseModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class News_Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "News Categories"

class Gallery_Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "Gallery Categories"

class News(BaseModel):

    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(upload_to = 'images/blog/%Y/%m/%d', blank=True, null=True)
    category = models.ForeignKey(News_Category, related_name='news_cat', on_delete=models.SET_DEFAULT, default="School")
    content = models.TextField()
    mins_read = models.IntegerField(default=3)
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)


    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }

        return reverse('blog-detail', kwargs=kwargs)

    class Meta:

        ordering = ['-created_on']
        verbose_name_plural = "News"

    def get_short(self):

        return self.content [:300]

    def __str__(self):

        return self.title


class Gallery(BaseModel):

    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'images/Gallery/%Y/%m/%d')
    category = models.ForeignKey(Gallery_Category, related_name='ga_cat', on_delete=models.SET_DEFAULT, default="School")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Gallery"
         
    def __str__(self):
        return self.title


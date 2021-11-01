from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS = (
        (0, "Draft"), 
        (1, "Publish")
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    introduction = models.TextField()
    cover_image = models.ImageField(upload_to=f"images/")
    cover_image_alt = models.TextField(max_length=200, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    posts = models.ManyToManyField('Post', related_name='article')
    categories = models.ManyToManyField('Category', related_name='article')
    views = models.IntegerField(default=0)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']    
    
    def __str__(self):
        return self.title
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Post(models.Model):
    STATUS = (
        (0, "Draft"), 
        (1, "Publish")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    display_image = models.ImageField(upload_to=f"images/")
    display_image_alt = models.TextField(max_length=200, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField('Category', related_name='posts')
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
    
    def __str__(self):
        return self.title
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
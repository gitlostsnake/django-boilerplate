# django-boilerplate README

This is a barebones project that frontend wise is very basic. The backend is currently on Sqlite but I will be changing that into postgres when used in a project.

The goal for my boilerplate is to eliminate the need to re-write the basic functions required for most sites. So I can focus on building project specifics which I find are a little more fun to work on.

### Features

#### User accounts
  1. login and Sign Up
  2. Email Authentication capable
     This works with SendInBlue's api. Currently not active because you need a Email Api key from them to make this work. 
     This is something that would be in your local_settings.py file which will be git ignored in production. 

#### Blog

For the blog I have made an 'Article' model and a 'Post' model. 

##### Article Model
```
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
```
In the Article model we have a 'posts' variable that tracks what posts are going to be included in each Article. Posts can be part of many differnt articles and the articles can have many different posts included. Each post is included in the article_view.html template after the Article's introduction and cover image. Currently the Posts are ordered by pub_date. The post Published first is shown first. 


##### Post Model
```
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
```

In my past projects I wanted to add in more images to my blog posts and instead of using something like Wagtail or another CMS instead I have just created a Many to Many relationship with the article and post models which is stored in the article model. This way I can have a longer article with many Images and each post has its own categories that is displayed in the article view. For example if a post touches on a subject that is slightly side tracked from the majority of the article you can search for other articles that are more inline with this category.

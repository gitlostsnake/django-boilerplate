# django-boilerplate

This is a barebones project that frontend wise is very basic. The backend is currently on Sqlite but I will be changing that into postgres when used in a project.

The goal for my boilerplate is to eliminate the need to re-write the basic functions required for most sites. So I can focus on building project specifics which I find are a little more fun to work on.


## Table of Contents
* [Set up](#set-up)
* [Technologies used](#technologies-used)
* [Features](#features)
    1. [User accounts](#user-accounts)
    2. [Blog](#blog)
        * [Article model](#article-model)
        * [Post model](#post-model)
    3. [Services and Selectors](#services-and-selectors)
* [Room for Improvement](#room-for-improvement)


### Set up
  1. Clone/pull/download this repository
  2. Install pipenv by running `pip install pipenv` in the terminal
  3. Create a virtual enviroment by running `pipenv shell` in the terminal
  4. Install all dependencies by running `pipenv install --dev`
     > More info on pipenv [_here_](https://realpython.com/pipenv-guide/)
  
### Optional
For emailing Go to the sendinblue website and continue the steps
> Send in blue's docs reference [_here_](https://developers.sendinblue.com/docs)
  
1. Get access to your api key.
2. Create a emailing template for signing up to the website
3. Create a list where you will keep all your users in

*  Go to the accounts/services.py file       
    1. In `def authenticate_new_user()` you will find the `send_smtp_email` variable. Change the template_id to your template id. 
        > `sib_api_v3_sdk.SendSmtpEmail(to=[params], template_id= YOUR TEMPLATE ID)`
        
    2. In `def activate_new_user()` you will change the the list ids to match with yours in the `payload` variable.
        > `payload = f'{{"email":"{email}", "listIds": [{YOUR LIST ID1}, {YOUR LIST ID2}]}}'`
     


### Technologies Used
1. Bootstrap
2. Bootstrap crispy forms 
3. Pytz
4. Send in blue Emailing API


### Features
* #### User accounts
  1. login and Sign Up
  2. Email Authentication capable
     This works with SendInBlue's api. Currently not active because you need a Email Api key from them to make this work. 
     This is something that would be in your local_settings.py file which will be git ignored in production. 

* #### Blog

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

* #### Services and Selectors
    I have added in two files into most app directories. Services for all Business logic and Selectors for my filters and database queries. This is to keep my views.py file looking cleaner and making it easier to read. Instead of seing a load of queries and model instance saves in a view file. You will see things like `signup_new_user(signup_form)` or `authenticate_new_user(request, user_id, template_id)` (template id is used in the Send In Blue api for email authentication) and `activate_new_user(request, uid64, token)` in the views instead. For basic filters and model changes it might seem like over kill but further into development if I'm working on a complicated feature. It's really helped the readability of my views.py file and kept my mind a little less cluttered keeping track of a huge view function. 


### Room for Improvement
* Password reset email is not implemented yet
* Including a front end framework like react
* Add in a checkout and payment method using stripes Api
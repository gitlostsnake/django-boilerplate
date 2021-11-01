from django.contrib import admin
from .models import Post, Article, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'pub_date', 'last_modified')
    list_filter = ("status", "categories")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'pub_date')
    list_filter = ("status", "categories")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
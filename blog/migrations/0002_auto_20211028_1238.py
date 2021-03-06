# Generated by Django 3.2.7 on 2021-10-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='article', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='hello', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]

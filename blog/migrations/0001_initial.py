# Generated by Django 3.2.7 on 2021-10-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('display_image', models.ImageField(upload_to='blog/post/<django.db.models.fields.CharField>/display_image/')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('categories', models.ManyToManyField(related_name='posts', to='blog.Category')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('cover_image', models.ImageField(upload_to='blog/article/<django.db.models.fields.CharField>/cover_image/')),
                ('cover_image_alt', models.TextField(max_length=200, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ManyToManyField(related_name='article', to='blog.Post')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]

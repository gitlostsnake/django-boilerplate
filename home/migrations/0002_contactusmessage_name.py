# Generated by Django 3.2.7 on 2021-09-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusmessage',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

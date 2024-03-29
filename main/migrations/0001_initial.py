# Generated by Django 3.2 on 2023-02-03 22:35

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Gallery Categories',
            },
        ),
        migrations.CreateModel(
            name='News_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'News Categories',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/blog/%Y/%m/%d')),
                ('content', models.TextField()),
                ('mins_read', models.IntegerField(default=3)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('category', models.ForeignKey(default='School', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='news_cat', to='main.news_category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/Gallery/%Y/%m/%d')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('category', models.ForeignKey(default='School', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='ga_cat', to='main.gallery_category')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'ordering': ['-created_on'],
            },
        ),
    ]

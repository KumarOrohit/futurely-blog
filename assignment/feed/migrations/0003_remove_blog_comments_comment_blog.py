# Generated by Django 4.1.3 on 2022-12-06 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_comment_blog_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.blog'),
        ),
    ]

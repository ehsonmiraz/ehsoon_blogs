# Generated by Django 5.0.2 on 2024-03-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_article_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='subtitle',
        ),
    ]

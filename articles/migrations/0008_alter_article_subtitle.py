# Generated by Django 5.0.2 on 2024-03-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default=' ', max_length=120),
        ),
    ]
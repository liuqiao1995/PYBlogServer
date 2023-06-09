# Generated by Django 3.2.19 on 2023-06-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(help_text='分类', max_length=255, unique=True, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(help_text='标签', max_length=255, unique=True, verbose_name='标签'),
        ),
    ]

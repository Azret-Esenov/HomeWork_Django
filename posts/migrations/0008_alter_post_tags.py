# Generated by Django 5.0.7 on 2024-08-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='posts.tag'),
        ),
    ]

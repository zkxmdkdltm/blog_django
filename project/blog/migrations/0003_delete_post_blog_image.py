# Generated by Django 4.0.4 on 2022-04-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

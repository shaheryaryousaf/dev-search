# Generated by Django 3.2.8 on 2021-10-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211026_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='project.png', null=True, upload_to='projects/%Y/%M/%D/'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/%Y/%M/%D/'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-28 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_review_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title'], 'verbose_name_plural': 'Projects'},
        ),
    ]

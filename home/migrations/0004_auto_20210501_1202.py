# Generated by Django 3.1.8 on 2021-05-01 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0003_auto_20210430_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_us_image',
            field=models.ForeignKey(help_text='Select an image to use for the about section on the homepage', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_us_text',
            field=models.TextField(default='', help_text='Enter a small description of the company'),
        ),
    ]

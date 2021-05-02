# Generated by Django 3.1.8 on 2021-05-02 18:31

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('dentist', '0002_auto_20210502_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentistpage',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='dentistpage',
            name='about',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Enter title', max_length=50)), ('text', wagtail.core.blocks.RichTextBlock())]))]),
        ),
    ]

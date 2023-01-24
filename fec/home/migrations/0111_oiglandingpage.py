# Generated by Django 2.2.16 on 2021-01-06 17:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0110_auto_20200930_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='OigLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_message', wagtail.fields.RichTextField(null=True)),
                ('complaint_url', models.URLField(blank=True, max_length=255, verbose_name='Complaint URL')),
                ('show_info_message', models.BooleanField(help_text='☑︎ display informational message | ☐ hide message')),
                ('info_message', wagtail.fields.RichTextField(blank=True, null=True)),
                ('stats_content', wagtail.fields.RichTextField(blank=True, help_text='If this section is empty, the logo will be shown (for screens larger than phones)', null=True)),
                ('recent_reports_url', models.URLField(blank=True, max_length=255, verbose_name='All reports URL')),
                ('resources', wagtail.fields.StreamField([('html', wagtail.blocks.RawHTMLBlock(label='OIG resources'))], blank=True, null=True)),
                ('you_might_also_like', wagtail.fields.StreamField([('group_0', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock())]), icon='list-ul', label='Group/column 1')), ('group_1', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock())]), icon='list-ul', label='Group/column 2')), ('group_2', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock())]), icon='list-ul', label='Group/column 3'))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

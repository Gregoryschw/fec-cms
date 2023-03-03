# Generated by Django 3.2.16 on 2023-02-27 05:19

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0124_auto_20220706_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('offices', wagtail.fields.StreamField([('office_title', wagtail.blocks.CharBlock()), ('office_description', wagtail.blocks.RichTextBlock(blank=True)), ('contact_info', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('item_label', wagtail.blocks.CharBlock(required=False)), ('item_icon', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.blocks.RichTextBlock(required=True))])))]), icon='', template='')), ('employee', wagtail.blocks.StructBlock([('employee_name', wagtail.blocks.CharBlock(blank=True)), ('employee_title', wagtail.blocks.CharBlock(blank=True)), ('employee_image', wagtail.images.blocks.ImageChooserBlock(blank=True)), ('employee_bio', wagtail.blocks.RichTextBlock(blank=True))])), ('sub_offices', wagtail.blocks.RichTextBlock(blank=True))], blank=True, null=True, use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

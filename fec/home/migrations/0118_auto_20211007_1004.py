# Generated by Django 3.1.13 on 2021-10-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0117_auto_20210907_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='category',
            field=models.CharField(choices=[('audit report', 'Audit report'), ('inspection or special review report', 'Inspection or special review report'), ('investigations', 'Investigations'), ('other reports and plans - oig', 'Other reports and plans - OIG'), ('semiannual report', 'Semiannual report'), ('strategic plan - oig', 'Strategic plan - OIG'), ('work plan', 'Work plan'), ('agency financial report', 'Agency Financial Report'), ('congressional submission', 'Congressional submission'), ('performance and accountability report', 'Performance and accountability report'), ('strategic plan', 'Strategic plan'), ('summary of performance and financial information', 'Summary of performance and financial information'), ('annual report', 'Annual report'), ('summary report', 'Summary report'), ('privacy act notice', 'Privacy Act notice'), ('privacy policy', 'Privacy policy'), ('buy america report', 'Buy America report'), ('fair act', 'FAIR Act'), ('public procurement report', 'Public procurement report'), ('anniversary report', 'Anniversary report'), ('gift report', 'Gift report'), ('shutdown plan', 'Shutdown plan'), ('study', 'Study'), ('other reports and plans', 'Other reports and plans')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='category',
            field=models.CharField(blank=True, choices=[('audit report', 'Audit report'), ('inspection or special review report', 'Inspection or special review report'), ('investigations', 'Investigations'), ('other reports and plans - oig', 'Other reports and plans - OIG'), ('semiannual report', 'Semiannual report'), ('strategic plan - oig', 'Strategic plan - OIG'), ('work plan', 'Work plan'), ('agency financial report', 'Agency Financial Report'), ('congressional submission', 'Congressional submission'), ('performance and accountability report', 'Performance and accountability report'), ('strategic plan', 'Strategic plan'), ('summary of performance and financial information', 'Summary of performance and financial information'), ('annual report', 'Annual report'), ('summary report', 'Summary report'), ('privacy act notice', 'Privacy Act notice'), ('privacy policy', 'Privacy policy'), ('buy america report', 'Buy America report'), ('fair act', 'FAIR Act'), ('public procurement report', 'Public procurement report'), ('anniversary report', 'Anniversary report'), ('gift report', 'Gift report'), ('shutdown plan', 'Shutdown plan'), ('study', 'Study'), ('other reports and plans', 'Other reports and plans')], help_text='If this is a report, add a category', max_length=255, null=True),
        ),
    ]

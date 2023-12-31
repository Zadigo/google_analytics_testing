# Generated by Django 4.1.3 on 2023-02-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SEOVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(default=0)),
                ('modified_on', models.DateField(auto_now_add=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('author', models.CharField(blank=True, help_text='Author or founder of the company', max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('keywords', models.CharField(blank=True, help_text='Meta keywords', max_length=100, null=True)),
                ('description', models.TextField(blank=True, help_text='Description of the company', max_length=300, null=True)),
                ('theme_color', models.CharField(blank=True, default='2d2d2d', max_length=20, null=True)),
            ],
            options={
                'ordering': ['version'],
                'abstract': False,
            },
        ),
    ]

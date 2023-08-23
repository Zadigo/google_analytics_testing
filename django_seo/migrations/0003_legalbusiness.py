# Generated by Django 4.1.3 on 2023-04-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_seo', '0002_alter_seoversion_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(default=0)),
                ('modified_on', models.DateField(auto_now_add=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('legal_name', models.CharField(blank=True, max_length=100, null=True)),
                ('general_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('customer_service_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telephone', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line', models.CharField(blank=True, max_length=300, null=True)),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('linkedin', models.URLField(blank=True, help_text='LinkedIn business page', null=True)),
                ('facebook', models.URLField(blank=True, help_text='Facebook business page', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Instagram profile page', null=True)),
                ('twitter', models.URLField(blank=True, help_text='Twitter business page', null=True)),
                ('youtube', models.URLField(blank=True, help_text='YouTube channel', null=True)),
                ('tiktok', models.URLField(blank=True, help_text='Tiktok page', null=True)),
            ],
            options={
                'verbose_name_plural': 'legal businesses',
                'ordering': ['version'],
            },
        ),
    ]
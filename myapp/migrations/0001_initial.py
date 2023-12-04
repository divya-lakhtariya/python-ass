# Generated by Django 4.2.7 on 2023-12-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.PositiveIntegerField(blank=True)),
                ('blog_title', models.CharField(blank=True, max_length=100)),
                ('blog_contact', models.CharField(blank=True, max_length=100)),
                ('blog_created', models.PositiveIntegerField(blank=True)),
                ('blog_updated', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
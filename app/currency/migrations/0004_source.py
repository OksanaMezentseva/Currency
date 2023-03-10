# Generated by Django 4.1.6 on 2023-03-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('source_url', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=65, null=True)),
                ('phone', models.CharField(max_length=65, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

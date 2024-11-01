# Generated by Django 4.2.1 on 2024-10-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('tracking_hash', models.CharField(max_length=64, unique=True)),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('opened', 'Opened'), ('failed', 'Failed')], default='sent', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

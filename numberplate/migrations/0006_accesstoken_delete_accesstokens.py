# Generated by Django 5.0.1 on 2024-02-06 23:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numberplate', '0005_accesstokens_created_at_accesstokens_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(default=uuid.uuid4, max_length=255, verbose_name='Access Token')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name_plural': 'Access Tokens',
            },
        ),
        migrations.DeleteModel(
            name='Accesstokens',
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-28 17:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resume', models.CharField(blank=True, max_length=500, null=True)),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
            },
        ),
    ]

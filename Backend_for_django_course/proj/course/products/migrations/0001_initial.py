# Generated by Django 4.2.5 on 2024-01-13 13:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('rand_token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]

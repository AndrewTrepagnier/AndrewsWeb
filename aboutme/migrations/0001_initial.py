# Generated by Django 5.0.6 on 2024-05-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Recommenders', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]

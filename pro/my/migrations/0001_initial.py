# Generated by Django 4.2.7 on 2024-02-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('month', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

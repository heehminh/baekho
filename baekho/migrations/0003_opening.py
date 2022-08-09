# Generated by Django 2.2 on 2022-08-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baekho', '0002_country_name_eng'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
    ]
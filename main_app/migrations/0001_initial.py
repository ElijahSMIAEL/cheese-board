# Generated by Django 4.1 on 2022-08-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('brand', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]

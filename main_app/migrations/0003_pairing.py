# Generated by Django 4.1 on 2022-08-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('type', models.CharField(choices=[('W', 'Wine'), ('F', 'Fruit'), ('C', 'Crackers'), ('Ch', 'Chocolate')], default='W', max_length=2)),
            ],
        ),
    ]

# Generated by Django 2.0.2 on 2018-02-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supllier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]

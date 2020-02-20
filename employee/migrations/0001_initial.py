# Generated by Django 3.0.2 on 2020-02-11 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
        ),
    ]
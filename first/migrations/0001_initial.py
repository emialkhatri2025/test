# Generated by Django 3.0.2 on 2020-01-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tips_calculator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.FloatField()),
                ('tax', models.FloatField()),
            ],
        ),
    ]

# Generated by Django 2.0.5 on 2018-07-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okada', '0004_auto_20180712_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='earthquake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Etitle', models.CharField(max_length=50)),
                ('Edatetime', models.CharField(max_length=50)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Moment', models.FloatField()),
                ('Magnitude', models.FloatField()),
                ('Depth', models.FloatField()),
                ('Strike', models.FloatField()),
                ('Dip', models.FloatField()),
                ('Rake', models.FloatField()),
            ],
        ),
    ]

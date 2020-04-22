# Generated by Django 2.2.5 on 2020-04-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disp_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('res_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

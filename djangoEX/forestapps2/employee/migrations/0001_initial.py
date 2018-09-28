# Generated by Django 2.1.1 on 2018-09-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empID', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contactName', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]

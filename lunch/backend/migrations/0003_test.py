# Generated by Django 3.1.2 on 2020-11-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20201102_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoge', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tests',
            },
        ),
    ]